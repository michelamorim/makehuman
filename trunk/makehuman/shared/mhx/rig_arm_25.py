#
#	Arm bone definitions
#

import mhx_rig
from mhx_rig import *

ArmJoints = [
	('hand_L_tail',			'j', 'r-finger-3-1'),
	('hand_R_tail',			'j', 'l-finger-3-1'),

	('r-uparm-front',		'v', 3440),
	('r-uparm-back',		'v', 3438),
	('r-uparm-over',		'v', 3014),
	('r-uparm-under',		'v', 3053),

	('l-uparm-front',		'v', 10175),
	('l-uparm-back',		'v', 10330),
	('l-uparm-over',		'v', 10712),
	('l-uparm-under',		'v', 10678),

	('r-loarm-mid',			'l', ((0.5, 'r-hand'), (0.5, 'r-elbow'))),
	('r-loarm-fan',			'l', ((0.25, 'r-hand'), (0.75, 'r-elbow'))),

	('l-loarm-mid',			'l', ((0.5, 'l-hand'), (0.5, 'l-elbow'))),
	('l-loarm-fan',			'l', ((0.25, 'l-hand'), (0.75, 'l-elbow'))),

	('r-clavicle-back',		'v', 2583),
	('r-clavicle-end',		'v', 2879),
	('l-clavicle-back',		'v', 11025),
	('l-clavicle-end',		'v', 10795),

	('r-pectoralis',		'v', 3341),
	('r-trapezeus-1',		'v', 2584),
	('r-trapezeus-2',		'v', 3633),
	('r-latdorsi',			'v', 4432),
	('r-deltoid',			'v', 2854),

	('l-pectoralis',		'v', 10410),
	('l-trapezeus-1',		'v', 11024),
	('l-trapezeus-2',		'v', 10159),
	('l-latdorsi',			'v', 9995),
	('l-deltoid'	,		'v', 10820),
	('l-deltoid'	,		'v', 10820),

	('r-shoulder-head',		'l', ((0.5, 'r-clavicle'), (0.5, 'r-trapezeus-1'))),
	('r-shoulder-vec',		'l', ((1, 'r-scapula'), (-1, 'r-shoulder-head'))),
	('r-shoulder-up-vec',	'X', ('r-shoulder-vec', (0,0,-1))),
	('r-shoulder-up-tail',	'l', ((1,'r-shoulder-head'), (1,'r-shoulder-up-vec'))),

	('l-shoulder-head',		'l', ((0.5, 'l-clavicle'), (0.5, 'l-trapezeus-1'))),
	('l-shoulder-vec',		'l', ((1, 'l-scapula'), (-1, 'l-shoulder-head'))),
	('l-shoulder-up-vec',	'X', ('l-shoulder-vec', (0,0,1))),
	('l-shoulder-up-tail',	'l', ((1,'l-shoulder-head'), (1,'l-shoulder-up-vec'))),

	('r-scapula-root',		'l', ((0.2, 'r-clavicle'), (0.8, 'r-clavicle-back'))),
	('r-scapula-top',		'v', 3048),
	('r-scapula-bot',		'v', 3600),

	('l-scapula-root',		'l', ((0.2, 'l-clavicle'), (0.8, 'l-clavicle-back'))),
	('l-scapula-top',		'v', 10683),
	('l-scapula-bot',		'v', 10192),

	('r-elbow-pt',			'o', ('r-elbow', [0,0,-3])),
	('l-elbow-pt',			'o', ('l-elbow', [0,0,-3])),
]

ArmHeadsTails = [
	# Shoulder
	('Shoulder_L',			'r-shoulder-head', 'r-shoulder'),
	('ShoulderScapula_L',	'r-shoulder', 'r-scapula'),
	('Clavicle_L',			'r-clavicle', 'r-scapula'),
	('Pectoralis_L',		'r-pectoralis', 'r-uparm-front'),
	('PectoralisTrg_L',		'r-uparm-front', ('r-uparm-front', yunit)),
	('Trapezeus-1_L',		'r-trapezeus-1', 'r-scapula'),
	('Trapezeus-2_L',		'r-trapezeus-2', 'r-uparm-back'),
	('LatDorsi_L',			'r-latdorsi', 'r-uparm-back'),
	('LatDorsiTrg_L',		'r-uparm-back', ('r-uparm-back', yunit)),
	('Deltoid_L',			'r-deltoid', 'r-uparm-over'),
	('DeltoidTrg_L',		'r-uparm-over', ('r-uparm-over', yunit)),

	('Shoulder_R',			'l-shoulder-head', 'l-shoulder'),
	('ShoulderScapula_R',	'l-shoulder', 'l-scapula'),
	('Clavicle_R',			'l-clavicle', 'l-scapula'),
	('Pectoralis_R',		'l-pectoralis', 'l-uparm-front'),
	('PectoralisTrg_R',		'l-uparm-front', ('l-uparm-front', yunit)),
	('Trapezeus-1_R',		'l-trapezeus-1', 'l-scapula'),
	('Trapezeus-2_R',		'l-trapezeus-2', 'l-uparm-back'),
	('LatDorsi_R',			'l-latdorsi', 'l-uparm-back'),
	('LatDorsiTrg_R',		'l-uparm-back', ('l-uparm-back', yunit)),
	('Deltoid_R',			'l-deltoid', 'l-uparm-over'),
	('DeltoidTrg_R',		'l-uparm-over', ('l-uparm-over', yunit)),

	# Deform
	('UpArmTwist_L',		'r-shoulder', 'r-elbow'),
	('UpArm_L',				'r-shoulder', 'r-elbow'),
	('LoArmUp_L',			'r-elbow', 'r-loarm-mid'),
	('LoArmFan_L',			'r-elbow', 'r-loarm-fan'),
	('LoArmDwn_L',			'r-elbow', 'r-hand'),
	('Hand_L',				'r-hand', 'hand_L_tail'),

	('UpArmTwist_R',		'l-shoulder', 'l-elbow'),
	('UpArm_R',				'l-shoulder', 'l-elbow'),
	('LoArmUp_R',			'l-elbow', 'l-loarm-mid'),
	('LoArmFan_R',			'l-elbow', 'l-loarm-fan'),
	('LoArmDwn_R',			'l-elbow', 'l-hand'),
	('Hand_R',				'l-hand', 'hand_R_tail'),

	# Rotation diffs
	('BendArmDown_L',		'r-shoulder', ('r-shoulder', (0,-1,0))),
	('BendArmDown_R',		'l-shoulder', ('l-shoulder', (0,-1,0))),
	('BendArmUp_L',			'r-shoulder', ('r-shoulder', (0,1,0))),
	('BendArmUp_R',			'l-shoulder', ('l-shoulder', (0,1,0))),
	('BendShoulderUp_L',	'r-shoulder-head', ('r-shoulder-head', (0,1,0))),
	('BendShoulderUp_R',	'l-shoulder-head', ('l-shoulder-head', (0,1,0))),
	
	# FK
	('UpArmFK_L',			'r-shoulder', 'r-elbow'),
	('LoArmFK_L',			'r-elbow', 'r-hand'),
	('HandFK_L',			'r-hand', 'hand_L_tail'),
	('UpArmFK_R',			'l-shoulder', 'l-elbow'),
	('LoArmFK_R',			'l-elbow', 'l-hand'),
	('HandFK_R',			'l-hand', 'hand_R_tail'),

	# IK
	('UpArmIK_L',			'r-shoulder', 'r-elbow'),
	('LoArmIK_L',			'r-elbow', 'r-hand'),
	('HandIK_L',			'r-hand', 'hand_L_tail'),
	('UpArmIK_R',			'l-shoulder', 'l-elbow'),
	('LoArmIK_R',			'l-elbow', 'l-hand'),
	('HandIK_R',			'l-hand', 'hand_R_tail'),

	# Pole Target
	('ElbowPTIK_L',			'r-elbow-pt', ('r-elbow-pt', yunit)),
	('ElbowPTIK_R',			'l-elbow-pt', ('l-elbow-pt', yunit)),
	('ElbowLinkPTIK_L',		'r-elbow', 'r-elbow-pt'),
	('ElbowLinkPTIK_R',		'l-elbow', 'l-elbow-pt'),
	('ElbowPTFK_L',			'r-elbow-pt', ('r-elbow-pt', yunit)),
	('ElbowPTFK_R',			'l-elbow-pt', ('l-elbow-pt', yunit)),
]

#upArmRoll = 1.69297
#loArmRoll = deg90
#handRoll = 1.22173

upArmRoll = 0.0
loArmRoll = 0.0
handRoll = 0.0

L_SHOULDER = L_ARMFK+L_ARMIK+L_SPINE

ArmArmature = [
	# Shoulder
	('Shoulder_L',			0.0, 'Spine3', F_WIR, L_SHOULDER, (1,1,1) ),
	('ShoulderScapula_L',	0.0, 'Shoulder_L', 0, L_HELP, (1,1,1) ),

	('Shoulder_R',			0.0, 'Spine3', F_WIR, L_SHOULDER, (1,1,1) ),
	('ShoulderScapula_R',	0.0, 'Shoulder_R', 0, L_HELP, (1,1,1) ),

	# Deform
	('UpArmTwist_L',	upArmRoll, 'Shoulder_L', F_DEF, L_DEF, (1,1,1) ),
	('UpArm_L',			upArmRoll, 'Shoulder_L', F_DEF, L_DEF, (1,1,1) ),
	('LoArmUp_L',		loArmRoll, 'UpArm_L', F_DEF, L_DEF, (1,1,1) ),
	('LoArmFan_L',		loArmRoll, 'UpArm_L', F_DEF, L_DEF, (1,1,1) ),
	('LoArmDwn_L',		loArmRoll, 'UpArm_L', F_DEF, L_DEF, (1,1,1) ),
	('Hand_L',			handRoll, 'LoArmDwn_L', F_DEF, L_DEF, (1,1,1) ),

	('UpArmTwist_R',	upArmRoll, 'Shoulder_R', F_DEF, L_DEF, (1,1,1) ),
	('UpArm_R',			upArmRoll, 'Shoulder_R', F_DEF, L_DEF, (1,1,1) ),
	('LoArmUp_R',		loArmRoll, 'UpArm_R', F_DEF, L_DEF, (1,1,1) ),
	('LoArmFan_R',		loArmRoll, 'UpArm_R', F_DEF, L_DEF, (1,1,1) ),
	('LoArmDwn_R',		loArmRoll, 'UpArm_R', F_DEF, L_DEF, (1,1,1) ),
	('Hand_R',			handRoll, 'LoArmDwn_R', F_DEF, L_DEF, (1,1,1) ),

	# Shoulder deform
	('Clavicle_L',			0.0, 'Spine3', F_DEF, L_DEF, (1,1,1) ),
	('Pectoralis_L',		0.0, 'Spine2', F_DEF, L_DEF, (1,1,1) ),
	('PectoralisTrg_L',		0.0, 'UpArmTwist_L', 0, L_HELP, (1,1,1) ),
	('Trapezeus-1_L',		0.0, 'Spine2', F_DEF, L_DEF, (1,1,1) ),
	('Trapezeus-2_L',		0.0, 'Spine2', F_DEF, L_DEF, (1,1,1) ),
	('LatDorsi_L',			0.0, 'Spine1', F_DEF, L_DEF, (1,1,1) ),
	('LatDorsiTrg_L',		0.0, 'UpArmTwist_L', 0, L_HELP, (1,1,1) ),
	('Deltoid_L',			0.0, 'Spine3', F_DEF, L_DEF, (1,1,1) ),
	('DeltoidTrg_L',		0.0, 'UpArmTwist_L', 0, L_HELP, (1,1,1) ),

	('Clavicle_R',			0.0, 'Spine3', F_DEF, L_DEF, (1,1,1) ),
	('Pectoralis_R',		0.0, 'Spine2', F_DEF, L_DEF, (1,1,1) ),
	('PectoralisTrg_R',		0.0, 'UpArmTwist_R', 0, L_HELP, (1,1,1) ),
	('Trapezeus-1_R',		0.0, 'Spine2', F_DEF, L_DEF, (1,1,1) ),
	('Trapezeus-2_R',		0.0, 'Spine2', F_DEF, L_DEF, (1,1,1) ),
	('LatDorsi_R',			0.0, 'Spine1', F_DEF, L_DEF, (1,1,1) ),
	('LatDorsiTrg_R',		0.0, 'UpArmTwist_R', 0, L_HELP, (1,1,1) ),
	('Deltoid_R',			0.0, 'Spine3', F_DEF, L_DEF, (1,1,1) ),
	('DeltoidTrg_R',		0.0, 'UpArmTwist_R', 0, L_HELP, (1,1,1) ),

	# Scapula
	#('Scapula_L',		0.0, 'Shoulder_L', F_DEF, L_DEF, (1,1,1) ),
	#('Scapula_R',		0.0, 'Shoulder_R', F_DEF, L_DEF, (1,1,1) ),

	# Rotation diffs
	('BendArmDown_L',		deg90, 'Shoulder_L', 0, L_HELP, (1,1,1)),
	('BendArmDown_R',		-deg90, 'Shoulder_R', 0, L_HELP, (1,1,1)),
	('BendArmUp_L',			-deg90, 'Shoulder_L', 0, L_HELP, (1,1,1)),
	('BendArmUp_R',			deg90, 'Shoulder_R', 0, L_HELP, (1,1,1)),
	('BendShoulderUp_L',	-deg90, 'Spine3', 0, L_HELP, (1,1,1)),
	('BendShoulderUp_R',	deg90, 'Spine3', 0, L_HELP, (1,1,1)),

	# FK
	('UpArmFK_L',		upArmRoll, 'Shoulder_L', F_WIR, L_ARMFK, (1,1,1) ),
	('LoArmFK_L',		loArmRoll, 'UpArmFK_L', F_WIR, L_ARMFK, (1,1,1) ),
	('HandFK_L',		handRoll, 'LoArmFK_L', F_WIR, L_ARMFK, (1,1,1) ),
	('UpArmFK_R',		-upArmRoll, 'Shoulder_R', F_WIR, L_ARMFK, (1,1,1) ),
	('LoArmFK_R',		-loArmRoll, 'UpArmFK_R', F_WIR, L_ARMFK, (1,1,1) ),
	('HandFK_R',		-handRoll, 'LoArmFK_R', F_WIR, L_ARMFK, (1,1,1) ),

	# IK 
	('UpArmIK_L',		upArmRoll, 'Shoulder_L', 0, L_ARMIK, (1,1,1) ),
	('LoArmIK_L',		loArmRoll, 'UpArmIK_L', 0, L_ARMIK, (1,1,1) ),
	('HandIK_L',		handRoll, None, F_WIR, L_ARMIK, (1,1,1)),
	('UpArmIK_R',		-upArmRoll, 'Shoulder_R', 0, L_ARMIK, (1,1,1) ),
	('LoArmIK_R',		-loArmRoll, 'UpArmIK_R', 0, L_ARMIK, (1,1,1) ),
	('HandIK_R',		-handRoll, None, F_WIR, L_ARMIK, (1,1,1)),

	# Pole target
	('ElbowPTIK_L',		0.0, 'Shoulder_L', F_WIR, L_ARMIK, (1,1,1)),
	('ElbowPTIK_R',		0.0, 'Shoulder_R', F_WIR, L_ARMIK, (1,1,1)),
	('ElbowLinkPTIK_L',	0.0, 'UpArmIK_L', F_RES, L_ARMIK, (1,1,1)),
	('ElbowLinkPTIK_R',	0.0, 'UpArmIK_R', F_RES, L_ARMIK, (1,1,1)),
	('ElbowPTFK_L',		0.0, 'UpArmFK_L', 0, L_HELP, (1,1,1)),
	('ElbowPTFK_R',		0.0, 'UpArmFK_R', 0, L_HELP, (1,1,1)),
]

#
#
#

limShoulder_L = (-deg30,deg90, -deg30,deg30,  -deg30,deg30)
limShoulder_R = (-deg30,deg90,  -deg30,deg30,  -deg30,deg30)

limUpArm_L = (-deg120,deg90, -100*deg1,deg45, -deg90,deg45)
limUpArm_R = (-deg120,deg90, -deg45,100*deg1, -deg45,deg90)

limLoArm_L = (0,0, -deg180,deg45, -135*deg1,0)
limLoArm_R = (0,0, -deg45,deg180, 0,135*deg1)

limHand_L = (-deg90,70*deg1, 0,0, -deg20,deg20)
limHand_R = (-deg90,70*deg1, 0,0, -deg20,deg20)

def ArmWritePoses(fp):
	# Shoulder
	addPoseBone(fp, 'Shoulder_L', 'GoboShldr_L', None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0,
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limShoulder_L, (True, True, True)])])

	addPoseBone(fp, 'Clavicle_L', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'ShoulderScapula_L', 'PLANE_X', 1])])

	addPoseBone(fp, 'Pectoralis_L', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'PectoralisTrg_L', 'PLANE_X', 0])])

	addPoseBone(fp, 'Trapezeus-1_L', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'ShoulderScapula_L', 'PLANE_X', 1])])

	addPoseBone(fp, 'Trapezeus-2_L', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'LatDorsiTrg_L', 'PLANE_X', 0])])

	addPoseBone(fp, 'LatDorsi_L', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'LatDorsiTrg_L', 'PLANE_X', 0])])

	addPoseBone(fp, 'Deltoid_L', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Up', 'DeltoidTrg_L', 'PLANE_X', 0])])


	addPoseBone(fp, 'Shoulder_R', 'GoboShldr_R', None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0,
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limShoulder_R, (True, True, True)])])

	addPoseBone(fp, 'Clavicle_R', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'ShoulderScapula_R', 'PLANE_X', 1])])

	addPoseBone(fp, 'Pectoralis_R', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'PectoralisTrg_R', 'PLANE_X', 0])])

	addPoseBone(fp, 'Trapezeus-1_R', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'ShoulderScapula_R', 'PLANE_X', 1])])

	addPoseBone(fp, 'Trapezeus-2_R', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'LatDorsiTrg_R', 'PLANE_X', 0])])

	addPoseBone(fp, 'LatDorsi_R', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Stretch', 'LatDorsiTrg_R', 'PLANE_X', 0])])

	addPoseBone(fp, 'Deltoid_R', None, None, (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('StretchTo', 0, 1, ['Up', 'DeltoidTrg_R', 'PLANE_X', 0])])

	'''
	# Scapula
	addPoseBone(fp, 'Scapula_L', None, None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0, [])

	addPoseBone(fp, 'Scapula_R', None, None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0, [])

	'''

	# Deform
	addPoseBone(fp, 'UpArmTwist_L', None, None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0,
		[('IK', 0, 1, ['IK', 'LoArmUp_L', 1, None, (True, False,True)]),
		 ('CopyRot', C_LOCAL, 0, ['Rot', 'UpArm_L', (0,1,0), (0,0,0), False])])

	addDeformLimb(fp, 'UpArm_L', 'UpArmIK_L', (1,1,1), 'UpArmFK_L', (1,1,1), 0, P_STRETCH)

	addPoseBone(fp, 'LoArmUp_L', None, None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0,
		[('IK', 0, 1, ['IK', 'Hand_L', 1, None, (True, False,True)]),
		 ('CopyRot', C_LOCAL, 0.5, ['Rot', 'LoArmDwn_L', (0,1,0), (0,0,0), False])])

	addPoseBone(fp, 'LoArmFan_L', None, None, (1,1,1), (1,0,1), (1,1,1), (1,1,1), 0,
		[('CopyRot', C_LOCAL, 0.5, ['Rot', 'LoArmUp_L', (1,0,1), (0,0,0), False])])

	addDeformLimb(fp, 'LoArmDwn_L', 'LoArmIK_L', (1,1,1), 'LoArmFK_L', (1,1,1), 0, P_STRETCH)

	addDeformLimb(fp, 'Hand_L', 'HandIK_L', (1,1,1), 'HandFK_L', (1,1,1), 0, 0)


	addPoseBone(fp, 'UpArmTwist_R', None, None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0,
		[('IK', 0, 1, ['IK', 'LoArmUp_R', 1, None, (True, False,True)]),
		 ('CopyRot', C_LOCAL, 0, ['Rot', 'UpArm_R', (0,1,0), (0,0,0), False])])

	addDeformLimb(fp, 'UpArm_R', 'UpArmIK_R', (1,1,1), 'UpArmFK_R', (1,1,1), 0, P_STRETCH)

	addPoseBone(fp, 'LoArmUp_R', None, None, (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0,
		[('IK', 0, 1, ['IK', 'Hand_R', 1, None, (True, False,True)]),
		 ('CopyRot', C_LOCAL, 0.5, ['Rot', 'LoArmDwn_R', (0,1,0), (0,0,0), False])])

	addPoseBone(fp, 'LoArmFan_R', None, None, (1,1,1), (1,0,1), (1,1,1), (1,1,1), 0,
		[('CopyRot', C_LOCAL, 0.5, ['Rot', 'LoArmUp_R', (1,0,1), (0,0,0), False])])

	addDeformLimb(fp, 'LoArmDwn_R', 'LoArmIK_R', (1,1,1), 'LoArmFK_R', (1,1,1), 0, P_STRETCH)

	addDeformLimb(fp, 'Hand_R', 'HandIK_R', (1,1,1), 'HandFK_R', (1,1,1), 0, 0)


	# FK
	addPoseBone(fp, 'UpArmFK_L', 'MHCircle025', 'FK_L', (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0, 
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limUpArm_L, (True, True, True)])])

	addPoseBone(fp, 'LoArmFK_L', 'MHCircle025', 'FK_L', (1,1,1), (1,0,0), (1,1,1), (1,1,1), 0,
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limLoArm_L, (True, True, True)])])

	addPoseBone(fp, 'HandFK_L', 'MHHand', 'FK_L', (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0,
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limHand_L, (True, True, True)])])
		

	addPoseBone(fp, 'UpArmFK_R', 'MHCircle025', 'FK_R', (1,1,1), (0,0,0), (1,1,1), (1,1,1), 0,
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limUpArm_R, (True, True, True)])])

	addPoseBone(fp, 'LoArmFK_R', 'MHCircle025', 'FK_R', (1,1,1), (1,0,0), (1,1,1), (1,1,1), 0, 
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limLoArm_R, (True, True, True)])])

	addPoseBone(fp, 'HandFK_R', 'MHHand', 'FK_R', (1,1,1), (0,1,0), (1,1,1), (1,1,1), 0, 
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limHand_R, (True, True, True)])])


	# IK

	addPoseBone(fp, 'UpArmIK_L', None, 'IK_L', (1,1,1), (0,0,0), (1,1,1), (1,1,1), P_STRETCH,
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limUpArm_L, (True, True, True)])])

	addPoseBone(fp, 'LoArmIK_L', None, 'IK_L', (1,1,1), (1,0,0), (1,1,1), (0,1,1), P_STRETCH,
		[('IK', 0, 1, ['IK', 'HandIK_L', 2, (pi, 'ElbowPTIK_L'), (True, False,True)]),
		#('CopyRot', C_LOCAL, 1, ['CopyRotY', 'HandIK_L', (0,1,0), (0,0,0), False]),
		('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limLoArm_L, (True, True, True)])
		])

	addPoseBone(fp, 'HandIK_L', 'GoboHandCtrl_L', 'IK_L', (0,0,0), (0,0,0), (1,1,1), (1,1,1), 0,
		mhx_rig.rootChildOfConstraints + [
		('ChildOf', C_CHILDOF, 0, ['Shoulder', 'Shoulder_L', (1,1,1), (1,1,1), (1,1,1)]),
		('LimitDist', 0, 'fNoStretch', ['Shoulder_L', 'Shoulder_L'])])


	addPoseBone(fp, 'UpArmIK_R', None, 'IK_R', (1,1,1), (0,0,0), (1,1,1), (1,1,1), P_STRETCH,
		[('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limUpArm_R, (True, True, True)])])

	addPoseBone(fp, 'LoArmIK_R', None, 'IK_R', (1,1,1), (1,0,0), (1,1,1), (0,1,1), P_STRETCH,
		[('IK', 0, 1, ['IK', 'HandIK_R', 2, (0, 'ElbowPTIK_R'), (True, False,True)]),
		#('CopyRot', C_LOCAL, 1, ['CopyRotY', 'HandIK_R', (0,1,0), (0,0,0), False]),
		('LimitRot', C_OW_LOCAL, 0, ['LimitRot', limLoArm_R, (True, True, True)])
		])

	addPoseBone(fp, 'HandIK_R', 'GoboHandCtrl_R', 'IK_R', (0,0,0), (0,0,0), (1,1,1), (1,1,1), 0, 
		mhx_rig.rootChildOfConstraints + [
		('ChildOf', C_CHILDOF, 0, ['Shoulder', 'Shoulder_R', (1,1,1), (1,1,1), (1,1,1)]),
		('LimitDist', 0, 'fNoStretch', ['Shoulder_R', 'Shoulder_R'])])

	# Pole target

	addPoseBone(fp, 'ElbowPTIK_L', 'MHCube025', 'IK_L', (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0, [])

	addPoseBone(fp, 'ElbowLinkPTIK_L', None, 'IK_L', (1,1,1), (1,1,1), (1,1,1), (1,1,1), P_STRETCH,
		[('StretchTo', 0, 1, ['Stretch', 'ElbowPTIK_L', 'PLANE_X', 0])])

	addPoseBone(fp, 'ElbowPTIK_R', 'MHCube025', 'IK_R', (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0, [])

	addPoseBone(fp, 'ElbowLinkPTIK_R', None, 'IK_R', (1,1,1), (1,1,1), (1,1,1), (1,1,1), P_STRETCH,
		[('StretchTo', 0, 1, ['Stretch', 'ElbowPTIK_R', 'PLANE_X', 0])])

	return
	
#
#	ArmWriteActions(fp)
#

def ArmWriteActions(fp):
	return

#
#	ArmFKIKDrivers
#	(Bone, FK constraint, IK constraint, driver, channel, max)
#

ArmFKIKDrivers = [
	("UpArm_L", True, ["RotFK", "StretchFK"], ["RotIK", "StretchIK"], "PArmIK_L", "LOC_X", 1.0),
	("LoArmDwn_L", True, ["RotFK", "StretchFK"], ["RotIK", "StretchIK"], "PArmIK_L", "LOC_X", 1.0),
	("Hand_L", True, ["RotFK"], ["RotIK"], "PArmIK_L", "LOC_X", 1.0),

	("UpArm_R", True, ["RotFK", "StretchFK"], ["RotIK", "StretchIK"], "PArmIK_R", "LOC_X", 1.0),
	("LoArmDwn_R", True, ["RotFK", "StretchFK"], ["RotIK", "StretchIK"], "PArmIK_R", "LOC_X", 1.0),
	("Hand_R", True, ["RotFK"], ["RotIK"], "PArmIK_R", "LOC_X", 1.0),
]

#
#	ArmDeformDrivers
#	(Bone, constraint, driver, rotdiff, keypoints)
#

ArmDeformDrivers = [
	("Deltoid_L", "Up", "min(a,3*(s-0.5))", 
		 [("a", "UpArmTwist_L", "BendArmUp_L"), ("s", "Shoulder_L", "BendShoulderUp_L")], 
			[(0,1), (90*deg1,1), (110*deg1,0)]),
	("Deltoid_R", "Up", "min(a,3*(s-0.5))", 
		 [("a", "UpArmTwist_R", "BendArmUp_R"), ("s", "Shoulder_R", "BendShoulderUp_R")], 
			[(0,1), (90*deg1,1), (110*deg1,0)])
]

#
#	ArmShapeDrivers
#	Shape : (driver, rotdiff, keypoints)
#

ArmShapeDrivers = {
	'BendArmDown_L' : ( 'UpArmTwist_L', 'BendArmDown_L',  [(0,1.5), (deg30,1), (deg90,0)] ),
	'BendArmDown_R' : ( 'UpArmTwist_R', 'BendArmDown_R',  [(0,1.5), (deg30,1), (deg90,0)] ),
	'BendArmUp_L' : ( 'UpArmTwist_L', 'BendArmUp_L',  [(0,1.5), (deg30,1), (deg90,0)] ),
	'BendArmUp_R' : ( 'UpArmTwist_R', 'BendArmUp_R',  [(0,1.5), (deg30,1), (deg90,0)] ),
}

#
#	ArmProcess
#	(bone, axis, angle)
#

ArmProcess = [
	("LoArmDwn_L", "Z", -deg20),
	("LoArmDwn_R", "Z", deg20),
	("LoArmUp_L", "Z", -deg20),
	("LoArmUp_R", "Z", deg20),
]	

ArmSnaps = [
	("LoArmFK_L", "LoArmDwn_L", 'Both'),
	("LoArmIK_L", "LoArmDwn_L", 'Both'),
	("HandFK_L", "Hand_L", 'Both'),
	("HandIK_L", "Hand_L", 'Both'),

	("LoArmFK_R", "LoArmDwn_R", 'Both'),
	("LoArmIK_R", "LoArmDwn_R", 'Both'),
	("HandFK_R", "Hand_R", 'Both'),
	("HandIK_R", "Hand_R", 'Both'),
]

ArmParents = [
]

ArmSelects = []

ArmRolls = []


