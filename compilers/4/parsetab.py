
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xb2\xfc\xb4\xf7\x19\x983\xec\x1b\xbae\x7f\x8e\xa7\xe4T'
    
_lr_action_items = {'TIMERANGE':([0,],[1,]),'DATA':([3,],[4,]),'QUERYDATA':([4,],[5,]),'CONDITION':([1,],[3,]),'$end':([2,5,],[0,-1,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[2,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> TIMERANGE CONDITION DATA QUERYDATA','expression',4,'p_expression_plus','chinese_sql.py',40),
]
