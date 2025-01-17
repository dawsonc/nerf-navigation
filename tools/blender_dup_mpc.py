

import bpy
import json
from mathutils import Matrix

import os.path

# pulls out specific frames of an animation into sepearte static collections

name_to_MPC = 'playground_mpc_2_mpc'
frames_to_save = [0, 8, 14] 

collection_to_work = bpy.data.collections[name_to_MPC]

toplevel_collection = bpy.data.collections.new("Static_"+name_to_MPC)
bpy.context.scene.collection.children.link(toplevel_collection)

for frame in range(0,15):
    bpy.context.scene.frame_set(frame)
    
    nc = bpy.data.collections.new("frame_"+str(frame)+"_"+name_to_MPC)
    toplevel_collection.children.link(nc)
    
    for obj in collection_to_work.objects:
        if "path_0" in obj.name or frame in frames_to_save:
            new_obj = obj.copy()
            nc.objects.link(new_obj)
            new_obj.animation_data_clear()
    

