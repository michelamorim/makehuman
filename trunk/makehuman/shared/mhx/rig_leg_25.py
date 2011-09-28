""" 
**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehuman.org/

**Code Home Page:**    http://code.google.com/p/makehuman/

**Authors:**           Thomas Larsson

**Copyright(c):**      MakeHuman Team 2001-2009

**Licensing:**         GPL3 (see also http://sites.google.com/site/makehumandocs/licensing)

**Coding Standards:**  See http://sites.google.com/site/makehumandocs/developers-guide

Abstract
--------
Leg bone definitions 

"""

import mhx_rig
from mhx_rig import *

offs = [0,0.6,0]
prcLegTrg = 0.2

LegJoints = [
    ('r-knee',              'f', ('r-knee-raw', 'r-upper-leg', 'r-ankle', [0,0,0.1])),
    ('l-knee',              'f', ('l-knee-raw', 'l-upper-leg', 'l-ankle', [0,0,0.1])),

    ('r-upleg1',            'l', ((1-bbMarg, 'r-upper-leg'), (bbMarg, 'r-knee'))),
    ('r-upleg2',            'l', ((0.5, 'r-upper-leg'), (0.5, 'r-knee'))),

    ('l-upleg1',            'l', ((1-bbMarg, 'l-upper-leg'), (bbMarg, 'l-knee'))),
    ('l-upleg2',            'l', ((0.5, 'l-upper-leg'), (0.5, 'l-knee'))),

    ('r-legtrg',            'l', ((1-prcLegTrg, 'r-upper-leg'), (prcLegTrg, 'r-knee'))),
    ('l-legtrg',            'l', ((1-prcLegTrg, 'l-upper-leg'), (prcLegTrg, 'l-knee'))),

    ('r-midfoot',           'l', ((0.5, 'r-ankle'), (0.5, 'r-foot-1'))),
    ('r-midtoe',            'l', ((0.5, 'r-foot-1'), (0.5, 'r-foot-2'))),
    ('l-midfoot',           'l', ((0.5, 'l-ankle'), (0.5, 'l-foot-1'))),
    ('l-midtoe',            'l', ((0.5, 'l-foot-1'), (0.5, 'l-foot-2'))),

    ('r-heel0',             'v', 5721),
    ('r-heel',              'p', ['r-foot-2', 'r-foot-1', 'r-heel0']),
    ('r-ankle-tip',         'o', ('r-ankle', [0.0, 0.0, -1.0])),
    ('r-loleg-fan',         'l', ((0.75, 'r-knee'), (0.25, 'r-ankle'))),

    ('l-heel0',             'v', 13338),
    ('l-heel',              'p', ['l-foot-2', 'l-foot-1', 'l-heel0']),
    ('l-ankle-tip',         'o', ('l-ankle', [0.0, 0.0, -1.0])),
    ('l-loleg-fan',         'l', ((0.75, 'l-knee'), (0.25, 'l-ankle'))),

    ('r-knee-pt',           'o', ('r-knee', [0,0,3])),
    ('l-knee-pt',           'o', ('l-knee', [0,0,3])),

    ('r-knee-head',         'v', 4500),
    ('r-knee-tail',         'v', 5703),
    ('l-knee-head',         'v', 6865),
    ('l-knee-tail',         'v', 6779),

    ('r-butt',              'v', 4475),
    ('l-butt',              'v', 6890),

    ('r-legback-head',      'vl', ((0.1, 6562), (0.9, 2120))),
    ('r-legback-tail',      'vl', ((0.1, 3942), (0.9, 3841))),
    ('l-legback-head',      'vl', ((0.1, 6750), (0.9, 7481))),
    ('l-legback-tail',      'vl', ((0.1, 7067), (0.9, 7168))),

    ('r-legout-head',       'vl', ((0.4, 3042), (0.6, 2929))),
    ('r-legout-tail',       'vl', ((0.7, 3973), (0.3, 3832))),
    ('l-legout-head',       'vl', ((0.4, 7280), (0.6, 7307))),
    ('l-legout-tail',       'vl', ((0.7, 7035), (0.3, 7177))),

    ('r-legfront-head',     'vl', ((0.8, 6562), (0.2, 4463))),
    ('r-legfront-tail',     'vl', ((0.7, 3942), (0.3, 3841))),
    ('l-legfront-head',     'vl', ((0.8, 6756), (0.2, 6902))),
    ('l-legfront-tail',     'vl', ((0.7, 7067), (0.3, 7168))),
    
    ('r-legin-head',        'vl', ((0.5, 6577), (0.5, 2134))),
    ('r-legin-tail',        'vl', ((0.2, 3973), (0.8, 3832))),
    ('l-legin-head',        'vl', ((0.5, 6733), (0.5, 7564))),
    ('l-legin-tail',        'vl', ((0.2, 7035), (0.8, 7177))),

    ('r-gastro-head',       'vl', ((0.2, 4105), (0.8, 5714))),
    ('r-gastro-tail',       'l', ((0.1, 'r-upper-leg'), (0.9, 'r-knee'))),
    ('l-gastro-head',       'vl', ((0.2, 6942), (0.8, 6768))),
    ('l-gastro-tail',       'l', ((0.1, 'l-upper-leg'), (0.9, 'l-knee'))),
]

LegHeadsTails = [
    # Hip = leg location
    ('Hip_L',           'r-upper-leg', ('r-upper-leg', ysmall)),
    ('Hip_R',           'l-upper-leg', ('l-upper-leg', ysmall)),

    # Leg
    ('UpLeg_L',         'r-upper-leg', 'r-knee'),
    ('LoLeg_L',         'r-knee', 'r-ankle'),
    ('Ankle_L',         'r-ankle', 'r-ankle-tip'),
    ('Foot_L',          'r-ankle', 'r-foot-1'),
    ('Toe_L',           'r-foot-1', 'r-foot-2'),
    ('LegIK_L',         'r-heel', 'r-foot-2'),
    ('LegFK_L',         'r-heel', 'r-foot-2'),
    ('ToeRev_L',        'r-foot-2', 'r-foot-1'),
    ('FootRev_L',       'r-foot-1', 'r-ankle'),
    
    ('UpLeg_R',         'l-upper-leg', 'l-knee'),
    ('LoLeg_R',         'l-knee', 'l-ankle'),
    ('Ankle_R',         'l-ankle', 'l-ankle-tip'),
    ('Foot_R',          'l-ankle', 'l-foot-1'),
    ('Toe_R',           'l-foot-1', 'l-foot-2'),
    ('LegIK_R',         'l-heel', 'l-foot-2'),
    ('LegFK_R',         'l-heel', 'l-foot-2'),
    ('ToeRev_R',        'l-foot-2', 'l-foot-1'),
    ('FootRev_R',       'l-foot-1', 'l-ankle'),

    # Deform 
    ('UpLeg1_L',        'r-upper-leg', 'r-upleg1'),
    ('DfmUpLeg2_L',     'r-upleg1', 'r-upleg2'),
    ('DfmUpLeg3_L',     'r-upleg2', 'r-knee'),
    ('DfmLoLeg_L',      'r-knee', 'r-ankle'),
    ('DfmLoLegFan_L',   'r-knee', 'r-loleg-fan'),
    ('DfmFoot_L',       'r-ankle', 'r-foot-1'),
    ('DfmToe_L',        'r-foot-1', 'r-foot-2'),

    ('UpLeg1_R',        'l-upper-leg', 'l-upleg1'),
    ('DfmUpLeg2_R',     'l-upleg1', 'l-upleg2'),
    ('DfmUpLeg3_R',     'l-upleg2', 'l-knee'),
    ('DfmLoLeg_R',      'l-knee', 'l-ankle'),
    ('DfmLoLegFan_R',   'l-knee', 'l-loleg-fan'),
    ('DfmFoot_R',       'l-ankle', 'l-foot-1'),
    ('DfmToe_R',        'l-foot-1', 'l-foot-2'),

    # Tweaks
    ('UpLegRot_L',      'r-upper-leg', 'r-legtrg'),
    ('UpLegRot_R',      'l-upper-leg', 'l-legtrg'),
    
    ('DfmButt_L',       'r-upper-leg', 'r-butt'),
    ('Butt_L',          'r-butt', ('r-butt', yunit)),
    ('DfmButt_R',       'l-upper-leg', 'l-butt'),
    ('Butt_R',          'l-butt', ('l-butt', yunit)),

    # Inverse stretching targets
    ('UpLeg3Inv_L',     'r-knee', 'r-upleg2'),
    ('UpLeg3Inv_R',     'l-knee', 'l-upleg2'),

    # Muscles
    ('DfmLegback_L',    'r-legback-head', 'r-legback-tail'),
    ('DfmLegback_R',    'l-legback-head', 'l-legback-tail'),
    ('DfmLegOut_L',     'r-legout-head', 'r-legout-tail'),
    ('DfmLegOut_R',     'l-legout-head', 'l-legout-tail'),
    ('DfmLegFront_L',   'r-legfront-head', 'r-legfront-tail'),
    ('DfmLegFront_R',   'l-legfront-head', 'l-legfront-tail'),
    ('DfmLegIn_L',      'r-legin-head', 'r-legin-tail'),
    ('DfmLegIn_R',      'l-legin-head', 'l-legin-tail'),
    ('DfmGastro_L',     'r-gastro-head', 'r-gastro-tail'),
    ('DfmGastro_R',     'l-gastro-head', 'l-gastro-tail'),

    ('LegbackTrg_L',    'r-upper-leg', 'r-legback-tail'),
    ('LegbackTrg_R',    'l-upper-leg', 'l-legback-tail'),
    ('LegOutTrg_L',     'r-knee', 'r-legout-tail'),
    ('LegOutTrg_R',     'l-knee', 'l-legout-tail'),
    ('LegFrontTrg_L',   'r-knee', 'r-legfront-tail'),
    ('LegFrontTrg_R',   'l-knee', 'l-legfront-tail'),
    ('LegInTrg_L',      'r-knee', 'r-legin-tail'),
    ('LegInTrg_R',      'l-knee', 'l-legin-tail'),
    ('GastroTrg_L',     'r-knee', 'r-gastro-tail'),
    ('GastroTrg_R',     'l-knee', 'l-gastro-tail'),

    # Knee deform
    ('DfmKnee_L',       'r-knee-head', 'r-knee-tail'),
    ('KneeTrg_L',       'r-knee-tail', ('r-knee-tail', ysmall)),
    ('DfmKnee_R',       'l-knee-head', 'l-knee-tail'),
    ('KneeTrg_R',       'l-knee-tail', ('l-knee-tail', ysmall)),

    # Pole Targets
    ('LegTrg_L',        'r-upper-leg', 'r-legtrg'),
    ('UpLeg1PT_L',      ('r-upleg1', (0,0,-1)), ('r-upleg1', (0,0,-2))),
    ('UpLeg2PT_L',      ('r-upleg2', (0,0,-1)), ('r-upleg2', (0,0,-2))),
    ('KneePT_L',        'r-knee-pt', ('r-knee-pt', offs)),
    ('KneeLinkPT_L',    'r-knee', 'r-knee-pt'),
    ('FootPT_L',        ('r-midfoot', (0,1,0.2)), ('r-midfoot', (0,1.3,0.2))),
    ('ToePT_L',         ('r-midtoe', (0,1,0)), ('r-midtoe', (0,1.3,0))),

    ('LegTrg_R',        'l-upper-leg', 'l-legtrg'),
    ('UpLeg1PT_R',      ('l-upleg1', (0,0,-1)), ('l-upleg1', (0,0,-2))),
    ('UpLeg2PT_R',      ('l-upleg2', (0,0,-1)), ('l-upleg2', (0,0,-2))),
    ('KneePT_R',        'l-knee-pt', ('l-knee-pt', offs)),
    ('KneeLinkPT_R',    'l-knee', 'l-knee-pt'),
    ('FootPT_R',        ('l-midfoot', (0,1,0.2)), ('l-midfoot', (0,1.3,0.2))),
    ('ToePT_R',         ('l-midtoe', (0,1,0)), ('l-midtoe', (0,1.3,0))),
]

#
#   LegArmature
#

upLegRoll = 0
loLegRoll = 0
footRoll = 0
#toeRoll = -63.5*D
toeRoll = 135*D
footCtrlRoll = 0.0

LegArmature = [
    # Leg
    ('Hip_L',          0, 'DfmHips', F_WIR, L_LTWEAK, NoBB),
    ('UpLeg_L',         upLegRoll, 'Hip_L', F_WIR, L_LLEGFK, NoBB),
    ('LoLeg_L',         loLegRoll, 'UpLeg_L', F_WIR, L_LLEGFK, NoBB),
    ('Foot_L',          footRoll, 'LoLeg_L', F_WIR+F_CON, L_LLEGFK, NoBB),
    ('Toe_L',           toeRoll, 'Foot_L', F_WIR, L_LLEGFK, NoBB),
    ('LegIK_L',         footCtrlRoll, Master, F_WIR, L_LLEGIK, NoBB),
    ('ToeRev_L',        0, 'LegIK_L', F_WIR, L_LLEGIK, NoBB),
    ('FootRev_L',       0, 'ToeRev_L', F_WIR, L_LLEGIK, NoBB),
    ('Ankle_L',         0, None, F_WIR, L_LTWEAK, NoBB),
    ('LegFK_L',         footCtrlRoll, 'LoLeg_L', 0, L_HELP, NoBB),

    ('Hip_R',          0, 'DfmHips', F_WIR, L_RTWEAK, NoBB),
    ('UpLeg_R',         -upLegRoll, 'Hip_R', F_WIR, L_RLEGFK, NoBB),
    ('LoLeg_R',         -loLegRoll, 'UpLeg_R', F_WIR, L_RLEGFK, NoBB),
    ('Foot_R',          -footRoll, 'LoLeg_R', F_WIR+F_CON, L_RLEGFK, NoBB),
    ('Toe_R',           -toeRoll, 'Foot_R', F_WIR, L_RLEGFK, NoBB),
    ('LegIK_R',         -footCtrlRoll, Master, F_WIR, L_RLEGIK, NoBB),
    ('ToeRev_R',        0, 'LegIK_R', F_WIR, L_RLEGIK, NoBB),
    ('FootRev_R',       0, 'ToeRev_R', F_WIR, L_RLEGIK, NoBB),
    ('Ankle_R',         0, None, F_WIR, L_RTWEAK, NoBB),
    ('LegFK_R',         footCtrlRoll, 'LoLeg_R', 0, L_HELP, NoBB),  
    
    # Tweaks
    ('UpLegRot_L',      0.0, 'Hip_L', F_WIR, L_LTWEAK, NoBB),
    ('UpLegRot_R',      0.0, 'Hip_R', F_WIR, L_RTWEAK, NoBB),

    # Pole targets
    ('LegTrg_L',        0.0, 'Hip_L', 0, L_HELP, NoBB),
    ('UpLeg1PT_L',      0.0, 'UpLegRot_L', 0, L_HELP, NoBB),
    ('UpLeg2PT_L',      0.0, 'UpLeg_L', 0, L_HELP, NoBB),
    ('KneePT_L',        0.0, None, F_WIR, L_LLEGIK, NoBB),
    ('KneeLinkPT_L',    0.0, 'UpLeg_L', F_RES, L_LLEGIK, NoBB),
    ('FootPT_L',        0.0, 'FootRev_L', 0, L_HELP, NoBB),
    ('ToePT_L',         0.0, 'ToeRev_L', 0, L_HELP, NoBB),

    ('LegTrg_R',        0.0, 'Hip_R', 0, L_HELP, NoBB),
    ('UpLeg1PT_R',      0.0, 'UpLegRot_R', 0, L_HELP, NoBB),
    ('UpLeg2PT_R',      0.0, 'UpLeg_R', 0, L_HELP, NoBB),
    ('KneePT_R',        0.0, None, F_WIR, L_RLEGIK, NoBB),
    ('KneeLinkPT_R',    0.0, 'UpLeg_R', F_RES, L_RLEGIK, NoBB),
    ('FootPT_R',        0.0, 'FootRev_R', 0, L_HELP, NoBB),
    ('ToePT_R',         0.0, 'ToeRev_R', 0, L_HELP, NoBB),

    # Deform
    ('UpLeg1_L',        upLegRoll, 'DfmHips', F_NOSCALE, L_DMAIN, NoBB),
    ('DfmUpLeg2_L',     upLegRoll, 'UpLeg1_L', F_DEF+F_CON+F_NOSCALE, L_DMAIN,(0,0,5) ),
    ('DfmUpLeg3_L',     upLegRoll, 'DfmUpLeg2_L', F_DEF+F_CON+F_NOSCALE, L_DMAIN, NoBB),
    ('DfmLoLeg_L',      loLegRoll, 'DfmUpLeg3_L', F_DEF+F_NOSCALE, L_DMAIN, NoBB),
    ('DfmLoLegFan_L',   loLegRoll, 'DfmUpLeg3_L', F_DEF, L_DEF, NoBB),
    ('DfmFoot_L',       footRoll, 'DfmLoLeg_L', F_DEF+F_CON, L_DMAIN, NoBB),
    ('DfmToe_L',        toeRoll, 'DfmFoot_L', F_DEF, L_DMAIN, NoBB),

    ('UpLeg1_R',        upLegRoll, 'DfmHips', F_NOSCALE, L_DMAIN, NoBB),
    ('DfmUpLeg2_R',     upLegRoll, 'UpLeg1_R', F_DEF+F_CON+F_NOSCALE, L_DMAIN,(0,0,5) ),
    ('DfmUpLeg3_R',     upLegRoll, 'DfmUpLeg2_R', F_DEF+F_CON+F_NOSCALE, L_DMAIN, NoBB),
    ('DfmLoLeg_R',      -loLegRoll, 'DfmUpLeg3_R', F_DEF+F_NOSCALE, L_DMAIN, NoBB),
    ('DfmLoLegFan_R',   -loLegRoll, 'DfmUpLeg3_R', F_DEF, L_DEF, NoBB),
    ('DfmFoot_R',       -footRoll, 'DfmLoLeg_R', F_DEF+F_CON, L_DMAIN, NoBB),
    ('DfmToe_R',        -toeRoll, 'DfmFoot_R', F_DEF, L_DMAIN, NoBB),

    # Inverse stretching targets
    ('UpLeg3Inv_L'  ,   0, 'UpLeg_L', 0, L_HELP, NoBB),
    ('UpLeg3Inv_R'  ,   0, 'UpLeg_R', 0, L_HELP, NoBB),

    # Butt
    ('Butt_L',          0.0, 'UpLeg1_L', F_WIR, L_LTWEAK, NoBB),
    ('DfmButt_L',       0.0, 'Hip_L', F_DEF, L_MSCL, NoBB),
    ('Butt_R',          0.0, 'UpLeg1_R', F_WIR, L_RTWEAK, NoBB),
    ('DfmButt_R',       0.0, 'Hip_R', F_DEF, L_MSCL, NoBB),

    # Muscles
    ('DfmLegback_L',    0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmLegback_R',    0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmLegOut_L',     0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmLegOut_R',     0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmLegFront_L',   0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmLegFront_R',   0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmLegIn_L',      0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmLegIn_R',      0, 'DfmHips', F_DEF, L_MSCL, NoBB),
    ('DfmGastro_L',     0, 'DfmLoLeg_L', F_DEF, L_MSCL, NoBB),
    ('DfmGastro_R',     0, 'DfmLoLeg_R', F_DEF, L_MSCL, NoBB),

    ('LegbackTrg_L',    0, 'UpLeg1_L', 0, L_HELP, NoBB),
    ('LegbackTrg_R',    0, 'UpLeg1_R', 0, L_HELP, NoBB),
    ('LegOutTrg_L',     0, 'UpLeg1_L', 0, L_HELP, NoBB),
    ('LegOutTrg_R',     0, 'UpLeg1_R', 0, L_HELP, NoBB),
    ('LegFrontTrg_L',   0, 'UpLeg1_L', 0, L_HELP, NoBB),
    ('LegFrontTrg_R',   0, 'UpLeg1_R', 0, L_HELP, NoBB),
    ('LegInTrg_L',      0, 'UpLeg1_L', 0, L_HELP, NoBB),
    ('LegInTrg_R',      0, 'UpLeg1_R', 0, L_HELP, NoBB),
    ('GastroTrg_L',     0, 'DfmUpLeg3_L', 0, L_HELP, NoBB),
    ('GastroTrg_R',     0, 'DfmUpLeg3_R', 0, L_HELP, NoBB),

    # Knee deform
    #('DfmKnee_L',       0, 'DfmUpLeg3_L', F_DEF, L_DEF, NoBB),
    #('KneeTrg_L',       0, 'LoLeg_L', 0, L_HELP, NoBB),
    #('DfmKnee_R',       0, 'DfmUpLeg3_R', F_DEF, L_DEF, NoBB),
    #('KneeTrg_R',       0, 'LoLeg_R', 0, L_HELP, NoBB),

]

#
#   LegControlPoses(fp):
#

limUpLeg_L = (-110*D,90*D, -90*D,90*D, -110*D,40*D)
limUpLeg_R = (-110*D,90*D, -90*D,90*D, -40*D,110*D)

limLoLeg_L = (-20*D,150*D,-40*D,40*D, -40*D,40*D)
limLoLeg_R = (-20*D,150*D,-40*D,40*D, -40*D,40*D)

limFoot_L = (-50*D,50*D, -40*D,40*D, -40*D,40*D)
limFoot_R = (-50*D,50*D, -40*D,40*D, -40*D,40*D)

limToe_L = (-20*D,60*D, 0,0, 0,0)
limToe_R = (-20*D,60*D, 0,0, 0,0)

limRevFoot_L = (-20*D,60*D, 0,0, 0,0)
limRevFoot_R = (-20*D,60*D, 0,0, 0,0)

limRevToe_L = (-10*D,45*D, 0,0, 0,0)
limRevToe_R = (-10*D,45*D, 0,0, 0,0)

#
#   Rotation modes
#   Dmod = Deform rig mode
#   Cmod = Control rig mode
#

DmodUpLeg = P_YZX
DmodLoLeg = P_YZX
DmodFoot = P_YZX
DmodToe = P_YZX

CmodUpLeg = 0
CmodLoLeg = 0
CmodFoot = 0
CmodToe = 0

def LegControlPoses(fp):

    addPoseBone(fp, 'Hip_L', 'MHBall025', None, (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0, [])

    addPoseBone(fp, 'Hip_R', 'MHBall025', None, (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0, [])

    addPoseBone(fp, 'UpLeg_L', 'GZM_Circle025', 'FK_L', (1,1,1), (0,0,0), (1,1,1), 
                ((1,1,1), (0,0,0), 0.05, None), CmodUpLeg, 
        [('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limUpLeg_L, (1,1,1)])])

    addPoseBone(fp, 'UpLeg_R', 'GZM_Circle025', 'FK_R', (1,1,1), (0,0,0), (1,1,1), 
                ((1,1,1), (0,0,0), 0.05, None), CmodUpLeg, 
        [('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limUpLeg_R, (1,1,1)])])

    deltaKnee = -2.5*D

    addPoseBone(fp, 'LoLeg_L', 'GZM_Circle025', 'FK_L', (1,1,1), (0,0,0), (1,1,1), 
                ((1,1,1), (0,0,0), 0.05, None), CmodLoLeg, 
        [('IK', 0, 0, ['LegIK', 'Ankle_L', 2, (-90*D+deltaKnee, 'KneePT_L'), (1,0,1)]),
        ('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limLoLeg_L, (1,1,1)])
        ])

    addPoseBone(fp, 'LoLeg_R', 'GZM_Circle025', 'FK_R', (1,1,1), (0,0,0), (1,1,1), 
                ((1,1,1), (0,0,0), 0.05, None), CmodLoLeg, 
        [('IK', 0, 0, ['LegIK', 'Ankle_R', 2, (-90*D-deltaKnee, 'KneePT_R'), (1,0,1)]),
        ('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limLoLeg_R, (1,1,1)])
        ])

    addPoseBone(fp, 'LegIK_L', 'MHFootCtrl_L', 'IK_L', (0,0,0), (0,0,0), (1,1,1), (1,1,1), 0,
        mhx_rig.rootChildOfConstraints + [
        ('ChildOf', C_CHILDOF, 0, ['Hip', 'Hip_L', (1,1,1), (1,1,1), (1,1,1)]),
        ('LimitDist', 0, 1, ['DistHip', 'Hip_L', 'LIMITDIST_INSIDE'])])

    addPoseBone(fp, 'LegIK_R', 'MHFootCtrl_R', 'IK_R', (0,0,0), (0,0,0), (1,1,1), (1,1,1), 0,
        mhx_rig.rootChildOfConstraints + [
        ('ChildOf', C_CHILDOF, 0, ['Hip', 'Hip_R', (1,1,1), (1,1,1), (1,1,1)]),
        ('LimitDist', 0, 1, ['DistHip', 'Hip_R', 'LIMITDIST_INSIDE'])])

    addPoseBone(fp, 'FootRev_L', 'MHRevFoot', 'IK_L', (1,1,1), (0,1,1), (1,1,1), (1,1,1), CmodFoot, 
        [('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limRevFoot_L, (1,1,1)])])

    addPoseBone(fp, 'FootRev_R', 'MHRevFoot', 'IK_R', (1,1,1), (0,1,1), (1,1,1), (1,1,1), CmodFoot,
        [('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limRevFoot_R, (1,1,1)])])

    addPoseBone(fp, 'ToeRev_L', 'MHRevToe', 'IK_L', (1,1,1), (0,1,1), (1,1,1), (1,1,1), CmodToe, 
        [('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limRevToe_L, (1,1,1)])])

    addPoseBone(fp, 'ToeRev_R', 'MHRevToe', 'IK_R', (1,1,1), (0,1,1), (1,1,1), (1,1,1), CmodToe, 
        [('LimitRot', C_OW_LOCAL, 1, ['LimitRot', limRevToe_R, (1,1,1)])])
    
    addPoseBone(fp, 'Foot_L', 'MHFoot', 'FK_L', (0,0,0), (0,1,1), (1,1,1), (1,1,1), CmodFoot, 
        [('IK', 0, 0, ['RevIK', 'FootRev_L', 1, (90*D, 'FootPT_L'), (1,0,1)]),
         #('CopyRot', C_LOCAL, 0, ['RevRot', 'FootRev_L', (0,1,0), (0,0,0), True]),
         ('IK', 0, 1, ['FreeIK', None, 2, None, (True, False,True)])])

    addPoseBone(fp, 'Foot_R', 'MHFoot', 'FK_R', (0,0,0), (0,1,1), (1,1,1), (1,1,1), CmodFoot, 
        [('IK', 0, 0, ['RevIK', 'FootRev_R', 1, (90*D, 'FootPT_R'), (1,0,1)]),
         #('CopyRot', C_LOCAL, 0, ['RevRot', 'FootRev_R', (0,1,0), (0,0,0), True]),
         ('IK', 0, 1, ['FreeIK', None, 2, None, (True, False,True)])])

    addPoseBone(fp, 'Toe_L', 'MHToe_L', 'FK_L', (1,1,1), (0,1,1), (1,1,1), (1,1,1), CmodToe, 
        [('IK', 0, 0, ['RevIK', 'ToeRev_L', 1, (90*D, 'ToePT_L'), (1,0,1)])])

    addPoseBone(fp, 'Toe_R', 'MHToe_R', 'FK_R', (1,1,1), (0,1,1), (1,1,1), (1,1,1), CmodToe, 
        [('IK', 0, 0, ['RevIK', 'ToeRev_R', 1, (90*D, 'ToePT_R'), (1,0,1)])])
    
    addPoseBone(fp, 'Ankle_L', 'MHBall025', 'IK_L', (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0,
        [('ChildOf', C_CHILDOF, 1, ['Foot', 'FootRev_L', (1,1,1), (1,1,1), (1,1,1)]) ])

    addPoseBone(fp, 'Ankle_R', 'MHBall025', 'IK_R', (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0,
        [('ChildOf', C_CHILDOF, 1, ['Foot', 'FootRev_R', (1,1,1), (1,1,1), (1,1,1)]) ])

    addPoseBone(fp, 'LegFK_L', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0, [])
    addPoseBone(fp, 'LegFK_R', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0, [])


    # Pole target

    addPoseBone(fp, 'KneePT_L', 'MHCube025', 'IK_L', (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0,
        [('ChildOf', C_CHILDOF, 1, ['Foot', 'LegIK_L', (1,1,1), (1,1,1), (1,1,1)]),
         ('ChildOf', C_CHILDOF, 0, ['Hip', 'Hip_L', (1,1,1), (1,1,1), (1,1,1)]) ])

    addPoseBone(fp, 'KneeLinkPT_L', None, 'IK_L', (1,1,1), (1,1,1), (1,1,1), (1,1,1), P_STRETCH,
        [('StretchTo', 0, 1, ['Stretch', 'KneePT_L', 0, 1])])

    addPoseBone(fp, 'LegTrg_L', None, 'FK_L', (1,1,1), (1,0,1), (1,1,1), (1,1,1), P_YXZ, 
         [('IK', 0, 1, ['LegIK', 'LoLeg_L', 1, None, (True, False,True)])])

    addPoseBone(fp, 'UpLegRot_L', 'GZM_Circle10', None, (1,1,1), (1,0,1), (1,1,1), (1,1,1), P_YXZ, 
         [('IK', 0, 1, ['LegIK', 'LoLeg_L', 1, None, (True, False,True)])])


    addPoseBone(fp, 'KneePT_R', 'MHCube025', 'IK_R', (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0, 
        [('ChildOf', C_CHILDOF, 1, ['Foot', 'LegIK_R', (1,1,1), (1,1,1), (1,1,1)]),
         ('ChildOf', C_CHILDOF, 0, ['Hip', 'Hip_R', (1,1,1), (1,1,1), (1,1,1)]) ])

    addPoseBone(fp, 'KneeLinkPT_R', None, 'IK_R', (1,1,1), (1,1,1), (1,1,1), (1,1,1), P_STRETCH,
        [('StretchTo', 0, 1, ['Stretch', 'KneePT_R', 0, 1])])

    addPoseBone(fp, 'LegTrg_R', None, 'FK_R', (1,1,1), (1,0,1), (1,1,1), (1,1,1), P_YXZ, 
         [('IK', 0, 1, ['LegIK', 'LoLeg_R', 1, None, (True, False,True)])])

    addPoseBone(fp, 'UpLegRot_R', 'GZM_Circle10', None, (1,1,1), (1,0,1), (1,1,1), (1,1,1), P_YXZ, 
         [('IK', 0, 1, ['LegIK', 'LoLeg_R', 1, None, (True, False,True)])])

    deltaUpLeg = 0

    # Deform 
    copyDeformPartial(fp, 'UpLeg1_L', 'UpLeg_L', (1,0,1), DmodUpLeg, U_LOC, None, 
        [('IK', 0, 1, ['IK', 'LoLeg_L', 1, (90*D-deltaUpLeg, 'UpLeg1PT_L'), (True, False,True)])])
    
    copyDeformPartial(fp, 'DfmUpLeg2_L', 'UpLeg_L', (1,1,1), DmodUpLeg, 0, None,
        [('StretchTo', 0, 1, ['Stretch', 'UpLeg3Inv_L', 1, 1])])
        
    copyDeformPartial(fp, 'DfmUpLeg3_L', 'UpLeg_L', (0,1,0), DmodUpLeg, 0, None, 
        [('IK', 0, 1, ['IK', 'LoLeg_L', 1, (90*D-deltaUpLeg, 'UpLeg2PT_L'), (True, False,True)])])

    copyDeform(fp, 'DfmLoLeg_L', 'LoLeg_L', DmodLoLeg, U_LOC+U_ROT, None,
        [('StretchTo', 0, 1, ['Stretch', 'Foot_L', 0, 1])])

    addPoseBone(fp, 'DfmLoLegFan_L', None, None, (1,1,1), (1,0,1), (1,1,1), (1,1,1), DmodLoLeg,
        [('CopyRot', 0, 0.5, ['Rot', 'LoLeg_L', (1,1,1), (0,0,0), False])])

    copyDeform(fp, 'DfmFoot_L', 'Foot_L', DmodFoot, U_LOC+U_ROT, None, [])

    copyDeform(fp, 'DfmToe_L', 'Toe_L', DmodToe, U_LOC+U_ROT, None, [])


    copyDeformPartial(fp, 'UpLeg1_R', 'UpLeg_R', (1,1,1), DmodUpLeg, U_LOC, None, 
        [('IK', 0, 1, ['IK', 'LoLeg_R', 1, (90*D+deltaUpLeg, 'UpLeg1PT_R'), (True, False,True)])])
    
    copyDeformPartial(fp, 'DfmUpLeg2_R', 'UpLeg_R', (1,1,1), DmodUpLeg, 0, None,
        [('StretchTo', 0, 1, ['Stretch', 'UpLeg3Inv_R', 1, 1])])
        
    copyDeformPartial(fp, 'DfmUpLeg3_R', 'UpLeg_R', (0,1,0), DmodUpLeg, 0, None,
        [('IK', 0, 1, ['IK', 'LoLeg_R', 1, (90*D+deltaUpLeg, 'UpLeg2PT_R'), (True, False,True)])])

    copyDeform(fp, 'DfmLoLeg_R', 'LoLeg_R', DmodLoLeg, U_LOC+U_ROT, None,
        [('StretchTo', 0, 1, ['Stretch', 'Foot_R', 0, 1])])

    addPoseBone(fp, 'DfmLoLegFan_R', None, None, (1,1,1), (1,0,1), (1,1,1), (1,1,1), DmodLoLeg,
        [('CopyRot', 0, 0.5, ['Rot', 'LoLeg_R', (1,1,1), (0,0,0), False])])

    copyDeform(fp, 'DfmFoot_R', 'Foot_R', DmodFoot, U_LOC+U_ROT, None, [])

    copyDeform(fp, 'DfmToe_R', 'Toe_R', DmodToe, U_LOC+U_ROT, None, [])

    # Tweak
    
    addPoseBone(fp, 'DfmButt_L', None, None, (1,1,1), (0,0,0), (0,0,0), (1,1,1), 0, 
    	[('StretchTo', C_STRVOL, 1, ['Stretch', 'Butt_L', 0, 1])])

    addPoseBone(fp, 'Butt_L', 'MHCube01', None, (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0, [])

    addPoseBone(fp, 'DfmButt_R', None, None, (1,1,1), (0,0,0), (0,0,0), (1,1,1), 0,
    	[('StretchTo', C_STRVOL, 1, ['Stretch', 'Butt_R', 0, 1])])

    addPoseBone(fp, 'Butt_R', 'MHCube01', None, (0,0,0), (1,1,1), (1,1,1), (1,1,1), 0, [])

    # Muscles

    addPoseBone(fp, 'DfmLegback_L', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegbackTrg_L', 1, 1])])

    addPoseBone(fp, 'DfmLegback_R', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegbackTrg_R', 1, 1])])

    addPoseBone(fp, 'DfmLegOut_L', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegOutTrg_L', 1, 1])])

    addPoseBone(fp, 'DfmLegOut_R', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegOutTrg_R', 1, 1])])

    addPoseBone(fp, 'DfmLegFront_L', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegFrontTrg_L', 1, 1])])

    addPoseBone(fp, 'DfmLegFront_R', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegFrontTrg_R', 1, 1])])

    addPoseBone(fp, 'DfmLegIn_L', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegInTrg_L', 1, 1])])

    addPoseBone(fp, 'DfmLegIn_R', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'LegInTrg_R', 1, 1])])

    addPoseBone(fp, 'DfmGastro_L', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'GastroTrg_L', 1, 5])])

    addPoseBone(fp, 'DfmGastro_R', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0,
        [('StretchTo', C_STRVOL, 1, ['Stretch', 'GastroTrg_R', 1, 5])])

    return
    
    # Knee deform

    addPoseBone(fp, 'DfmKnee_L', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), P_STRETCH,
        [('StretchTo', C_DEFRIG, 1, ['Stretch', 'KneeTrg_L', 0, 1])])

    addPoseBone(fp, 'DfmKnee_R', None, None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), P_STRETCH,
        [('StretchTo', C_DEFRIG, 1, ['Stretch', 'KneeTrg_R', 0, 1])])

    return

#
#   LegPropLRDrivers
#   (Bone, Name, Props, Expr)
#

LegPropLRDrivers = [
    ('LoLeg', 'LegIK', ['LegIk'], 'x1'),
    ('Foot', 'RevIK', ['LegIk', 'LegIkToAnkle'], 'x1*(1-x2)'),
    ('Foot', 'FreeIK', ['LegIk'], '1-x1'),
    ('Toe', 'RevIK', ['LegIk', 'LegIkToAnkle'], 'x1*(1-x2)'),
    ('LegIK', 'DistHip', ['LegStretch'], '1-x1'),
    ('KneePT', 'Foot', ['KneeFollowsFoot'], 'x1'),
    ('KneePT', 'Hip', ['KneeFollowsFoot'], '1-x1'),  
    ('Ankle', 'Foot', ['LegIkToAnkle'], '1-x1'),
]

LegPropDrivers = [
    ('UpLeg_L', 'LimitRot', ['RotationLimits'], 'x1'),
    ('LoLeg_L', 'LimitRot', ['RotationLimits'], 'x1'),    

    ('UpLeg_R', 'LimitRot', ['RotationLimits'], 'x1'),
    ('LoLeg_R', 'LimitRot', ['RotationLimits'], 'x1'),    
]

#
#   LegDeformDrivers
#   Bone : (constraint, driver, rotdiff, keypoints)
#

LegDeformDrivers = []

#
#   LegShapeDrivers
#   Shape : (driver, rotdiff, keypoints)
#

LegShapeDrivers = {
}




