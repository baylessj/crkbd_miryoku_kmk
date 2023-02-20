from kb import KMKKeyboard; keyboard = KMKKeyboard()
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.modtap import ModTap; keyboard.modules.append(ModTap())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord())

# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.STATIC,1:["1 2 3 4 5 6","","","","","","",""]},corner_two={0:OledReactionType.STATIC,1:[" 7 8 Layer","","","","","",""," 7 8 Layer"]},corner_three={0:OledReactionType.LAYER,1:["^","  ^","    ^","      ^","        ^","          ^","",""]},corner_four={0:OledReactionType.LAYER,1:["","","","","",""," ^","   ^"]}),toDisplay=OledDisplayMode.TXT,flip= True)
# oled
keyboard.extensions.append(oled_ext)

# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[18,209,123],[255,0,0],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[0,255,217],[0,255,217],[0,255,217],[255,0,0],[0,255,217],[0,255,217],[0,255,217],[0,255,217],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[0,25,255],[0,25,255],[255,0,0],[255,0,0],[0,255,77],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[0,255,77],[0,25,255],[0,255,77],[255,55,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,0]],split=True,rightSide=True,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)


split = Split(use_pio=True)
keyboard.modules.append(split)


keyboard.keymap = [
# BASE
[
KC.NO, KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT, KC.NO,
KC.NO, KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.R, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.S, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.T, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.M, KC.MT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.E, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.I, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.O, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.NO,
KC.NO, KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.MT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.MT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.NO,
KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200)
],
# EXTRA
[
KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.NO,
KC.NO, KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.H, KC.MT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.NO,
KC.NO, KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.MT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.MT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.NO,
KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200)
],
# TAP
[
KC.NO, KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT, KC.NO,
KC.NO, KC.A, KC.R, KC.S, KC.T, KC.G, KC.M, KC.N, KC.E, KC.I, KC.O, KC.NO,
KC.NO, KC.Z, KC.X, KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.DOT, KC.SLSH, KC.NO,
KC.ESC, KC.SPC, KC.TAB, KC.ENT, KC.BSPC, KC.DEL
],
# BUTTON
[
KC.NO, KC.NO, KC.LSFT(KC.DEL), KC.LCTL(KC.INS), KC.LSFT(KC.INS), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.NO, KC.LSFT(KC.DEL), KC.LCTL(KC.INS), KC.LSFT(KC.INS), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.NO,
KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB
],
# NAV
[
KC.NO, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.TD(KC.CW, KC.CAPS, tap_time=200), KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.NO,
KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.NO, KC.INS, KC.HOME, KC.PGDN, KC.PGUP, KC.END, KC.NO,
KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.DEL
],
# MOUSE
[
KC.NO, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT, KC.NO,
KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.NO, KC.NO, KC.NO, KC.MW_DN, KC.MW_UP, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB
],
# MEDIA
[
KC.NO, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.PS_TOG, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT, KC.NO,
KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.NO, KC.HID, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.MSTP, KC.MPLY, KC.MUTE
],
# NUM
[
KC.NO, KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.NO,
KC.NO, KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.RALT, KC.NO, KC.NO,
KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO, KC.NO
],
# SYM
[
KC.NO, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.NO,
KC.NO, KC.COLN, KC.DLR, KC.PERC, KC.CIRC, KC.PLUS, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.PIPE, KC.NO, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.RALT, KC.NO, KC.NO,
KC.LPRN, KC.RPRN, KC.UNDS, KC.NO, KC.NO, KC.NO
],
# FUN
[
KC.NO, KC.F12, KC.F7, KC.F8, KC.F9, KC.PSCR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.NO,
KC.NO, KC.F11, KC.F4, KC.F5, KC.F6, KC.SLCK, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.F10, KC.F1, KC.F2, KC.F3, KC.PAUS, KC.NO, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.RALT, KC.NO, KC.NO,
KC.APP, KC.SPC, KC.TAB, KC.NO, KC.NO, KC.NO
],

]

layer_names_list = [
"Base", "Extra", "Tap", "Button", "Nav", "Mouse", "Media", "Num", "Sym", "Fun",
]

if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)
