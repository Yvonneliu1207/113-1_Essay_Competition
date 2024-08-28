from nuscenes.nuscenes import NuScenes

nusc = NuScenes(version='v1.0-trainval', dataroot='/Users/yvonne/work/part5', verbose=True)

my_scene_token = nusc.field2token('scene', 'name', 'scene-0475')[0]

# Get records from DB.
scene_rec = nusc.get('scene', my_scene_token)

first_sample_token = scene_rec['first_sample_token']
my_sample = nusc.get('sample', first_sample_token)
nusc.render_sample_data(my_sample['data']['RADAR_FRONT'])

next_sample_token = my_sample['next']
my_sample = nusc.get('sample', next_sample_token)
nusc.render_sample_data(my_sample['data']['RADAR_FRONT'])

has_more_frames = True
while has_more_frames:    
    if not my_sample['next'] == "":
        next_sample_token = my_sample['next']
        my_sample = nusc.get('sample', next_sample_token)
        nusc.render_sample_data(my_sample['data']['RADAR_FRONT'])
    else:
        has_more_frames = False


