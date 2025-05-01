import open3d as o3d

def visualize_point_cloud(pcd, colors):
    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd], width=800, height=600)
