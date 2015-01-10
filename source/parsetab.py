
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x97Lt\xdf\xb0\x01\xc1i\x86Og\xd1E\x7f\xd8\x10'
    
_lr_action_items = {'H2':([0,17,],[2,2,]),'H3':([0,17,],[3,3,]),'H1':([0,17,],[4,4,]),'H6':([0,17,],[5,5,]),'H4':([0,17,],[6,6,]),'H5':([0,17,],[7,7,]),'TEXT':([2,3,4,5,6,7,],[10,10,10,10,10,10,]),'CR':([8,9,10,11,12,13,14,15,16,18,],[17,-2,-10,-5,-6,-4,-9,-7,-8,-3,]),'$end':([1,8,9,10,11,12,13,14,15,16,18,],[0,-1,-2,-10,-5,-6,-4,-9,-7,-8,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,],[1,]),'expression':([0,17,],[9,18,]),'statement':([0,],[8,]),'factor':([2,3,4,5,6,7,],[11,12,13,14,15,16,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> statement','body',1,'p_body','run.py',50),
  ('statement -> expression','statement',1,'p_state','run.py',55),
  ('statement -> statement CR expression','statement',3,'p_state','run.py',56),
  ('expression -> H1 factor','expression',2,'p_exp_cr','run.py',63),
  ('expression -> H2 factor','expression',2,'p_exp_cr','run.py',64),
  ('expression -> H3 factor','expression',2,'p_exp_cr','run.py',65),
  ('expression -> H4 factor','expression',2,'p_exp_cr','run.py',66),
  ('expression -> H5 factor','expression',2,'p_exp_cr','run.py',67),
  ('expression -> H6 factor','expression',2,'p_exp_cr','run.py',68),
  ('factor -> TEXT','factor',1,'p_factor_text','run.py',86),
]