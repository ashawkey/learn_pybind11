from asicp import asicp
import numpy as np
import math

import os
import glob

import open3d as o3d

def numpy2pc(x):
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(x)
    return pc
    
def plot(X, Y, Z):
    X = numpy2pc(X)
    Y = numpy2pc(Y)
    Z = numpy2pc(Z)
    X.paint_uniform_color([1, 0, 0]) # red, source
    Y.paint_uniform_color([0, 1, 0]) # yellow, target
    Z.paint_uniform_color([0, 0, 1]) # blue, transformed
    o3d.visualization.draw_geometries([X, Y, Z])

def random_transform(X):
    # X: [n, 3]
    m = np.eye(3)
    
    # rot
    theta = np.random.uniform(-0.25, 0.25) * math.pi # [-pi/4, pi/4]
    m = np.matmul(m, [[math.cos(theta), math.sin(theta), 0], [-math.sin(theta), math.cos(theta), 0], [0, 0, 1]])
    
    # scale
    scale = np.random.uniform(0.5, 2, size=(3))
    m = m @ np.diag(scale)

    # translate
    t = np.random.randn(1, 3) * 0.1

    return X @ m + t
    

def robust_asicp(X, Y, threshold, max_iterations, verbose):
    # remove outliers first, then only perform ICP with inliers.
    # need a rough align.
    # X, Y: [3, N], [3, M], assume N >> M (Y is incomplete)

    # However, this harms anisotropic scaling... and falls back to nomral ICP...
    dist = np.linalg.norm(X[:, :, None] - Y[:, None, :], axis=0) # [N, M]
    mask = dist.min(1) <= (threshold * 10)
    X_masked = X[:, mask]
    print(f'[Robust ICP] X: {X.shape[1]} --> {X_masked.shape[1]}')

    return asicp(X_masked, Y, threshold=threshold, max_iterations=max_iterations, verbose=verbose)



### test asicp with real cases !!!

root = '/data2/tang/pointgroup-exps/vae1_zunet/icp_tmp'

sources = sorted(glob.glob(os.path.join(root, 'source*.npy')))
targets = sorted(glob.glob(os.path.join(root, 'target*.npy')))

for i in range(len(sources)):
    X = np.load(sources[i])

    Y = np.load(targets[i])
    #Y = random_transform(X)

    print(X.shape, Y.shape)

    R, S, T, indices, rmse = asicp(X.T, Y.T, threshold=0.02, max_iterations=50, verbose=False)
    #R, S, T, indices, rmse = robust_asicp(X.T, Y.T, threshold=0.02, max_iterations=50, verbose=False)

    print(f'RMSE {rmse}')
    Z = (R @ S @ X.T + T[:, None]).T

    ### plot
    plot(X, Y, Z)
