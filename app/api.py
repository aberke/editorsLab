from flask import Flask, Blueprint, json, request, abort

from app.models import Comment

import twilio_tools


api = Blueprint('api', __name__)

@api.route('/')
def apiIndex():
	return "I'm an API"


# ******************* TWILIO BELOW **************************

# get twiml for recording the audio
@api.route('/twilio-record')
def twilio_record():
	print('**************** twilio-record ********')
	return twilio.record_twiml()

# Callback once recording is posted
@api.route('/handle-recording')
def handle_recording():
	print('*************** twilio handle-recording ******')
	recording_url = request.values.get("RecordingUrl", None)
	print('*** recording_url: ' + recording_url)
	return 'OK'

@api.route('/softphone-token')
def get_softphone_token():
	return twilio_tools.generate_capability_token()

# ******************* TWILIO ABOVE **************************


# **************** Castmembers ****************
@api.route('/castmember', methods=['DELETE'])
def httpDELETEcastmember():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	castmember = Castmember.query.filter_by(id=json.loads(request.data)['id']).first()
	db.session.delete(castmember)
	db.session.commit()
	return '200'

@api.route('/castmembers', methods=['GET'])
def httpGETcastmembers():
	castmembers = Castmember.query.all()
	return json.dumps(dbItems2DictList(castmembers))

@api.route('/castmember', methods=['POST'])
def httpPOSTcastmember():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	requestDict = json.loads(request.data)
	if not 'name' in requestDict: return abort(500)

	name = requestDict['name']
	role = requestDict['role'] if ('role' in requestDict) else 'Guest'
	twitter_handle = requestDict['twitter_handle'] if ('twitter_handle' in requestDict) else None

	new_castmember = Castmember(name=name, role=role, twitter_handle=twitter_handle)
	db.session.add(new_castmember)
	db.session.commit()

	return json.dumps(row2dict(new_castmember))

# **************** Castmembers above ****************

# **************** Tags ****************

@api.route('/tag', methods=['DELETE'])
def httpDELETETag():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	tag = Tag.query.filter_by(id=json.loads(request.data)['id']).first()
	db.session.delete(tag)
	db.session.commit()
	return '200'

@api.route('/tag', methods=['POST'])
def httpPOSTTag():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	requestDict = json.loads(request.data)
	if not 'label' in requestDict: return abort(500)

	new_tag = Tag(label=requestDict['label'])
	db.session.add(new_tag)
	db.session.commit()
	return json.dumps(row2dict(new_tag))


@api.route('/tags', methods=['GET'])
def httpGETtags():
	tags = Tag.query.all()
	return json.dumps(dbItems2DictList(tags))

# **************** Tags above****************

# **************** Episodes ****************

@api.route('/episode/order-down', methods=['PUT'])
def episode_order_down():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	requestDict = json.loads(request.data)
	episode = Episode.query.filter_by(id=requestDict['episode_id']).first()
	episode_order = episode.order
	if (episode_order == 0): # already 1st -- can't increase order
		abort(500)
	next_episode = Episode.query.filter_by(order=(episode_order - 1)).first()

	next_episode.order = episode_order
	episode.order = episode_order - 1
	db.session.commit()

	return json.dumps(all_episodes())

@api.route('/episode/order-up', methods=['PUT'])
def episode_order_up():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	requestDict = json.loads(request.data)
	episode = Episode.query.filter_by(id=requestDict['episode_id']).first()
	episode_order = episode.order
	if (episode_order == (Episode.query.count() - 1)): # already last -- can't increase order
		abort(500)
	next_episode = Episode.query.filter_by(order=(episode_order + 1)).first()

	next_episode.order = episode_order
	episode.order = episode_order + 1
	db.session.commit()

	return json.dumps(all_episodes())



@api.route('/episode/add-castmember', methods=['POST'])
def episode_add_castmember():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	requestDict = json.loads(request.data)
	episode = Episode.query.filter_by(id=requestDict['episode_id']).first()
	castmember = Castmember.query.filter_by(id=requestDict['castmember_id']).first()
	episode.castmembers.append(castmember)
	db.session.commit()
	return '200'

@api.route('/episode/add-tag', methods=['POST'])
def episode_add_tag():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	requestDict = json.loads(request.data)
	episode = Episode.query.filter_by(id=requestDict['episode_id']).first()
	tag = Tag.query.filter_by(id=requestDict['tag_id']).first()
	episode.tags.append(tag)
	db.session.commit()
	return '200'

@api.route('/episode', methods=['POST'])
def httpPOSTepisode():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	requestDict = json.loads(request.data)
	if ((not 'soundcloudID' in requestDict) or (not 'title' in requestDict) or (not 'description' in requestDict)):
		return abort(500)

	new_episode = Episode(soundcloudID=requestDict['soundcloudID'], title=requestDict['title'], description=requestDict['description'])
	db.session.add(new_episode)
	db.session.commit()
	return json.dumps(row2dict(new_episode))

@api.route('/episodes', methods=['GET'])
def httpGETepisodes():
	return json.dumps(all_episodes())

@api.route('/episode', methods=['DELETE'])
def httpDELETEepisode():
	if not auth.is_authenticated(): return json.dumps({'error': 'not authorized'}), '500'
	
	episode = Episode.query.filter_by(id=json.loads(request.data)['id']).first()
	db.session.delete(episode)
	db.session.commit()
	return '200'

# **************** Episodes above ****************


