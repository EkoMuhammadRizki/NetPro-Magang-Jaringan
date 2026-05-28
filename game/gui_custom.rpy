## ============================================================
## gui_custom.rpy — Kustomisasi UI Premium untuk NetPro TKJ
## ============================================================

## ─── WARNA TEMA UTAMA ─────────────────────────────────────────
## Definisi palet warna tema "Dark Tech" agar konsisten di seluruh UI game.

define ACCENT_BLUE    = "#00E5FF" # Warna aksen biru neon (Cyber)
define ACCENT_GOLD    = "#FFD700" # Warna aksen emas (Penting)
define DARK_BG        = "#0D1117" # Warna latar belakang gelap (GitHub style)
define PANEL_BG       = "#0F1923" # Warna latar belakang panel
define TEXT_PRIMARY   = "#E3F2FD" # Warna teks utama
define TEXT_MUTED     = "#78909C" # Warna teks redup/sekunder
define SUCCESS_COLOR  = "#76FF03" # Warna hijau untuk indikator sukses
define WARNING_COLOR  = "#FFD740" # Warna kuning untuk peringatan
define DANGER_COLOR   = "#FF5252" # Warna merah untuk error/bahaya

## ─── OVERRIDE GUI GLOBAL ──────────────────────────────────────

## Warna latar text box
init python:
    gui.text_color                = "#E0E0E0"
    gui.interface_text_color      = "#CCCCCC"
    gui.idle_color                = "#B0BEC5"
    gui.idle_small_color          = "#78909C"
    gui.hover_color               = "#00E5FF"
    gui.selected_color            = "#00E5FF"
    gui.insensitive_color         = "#455A64"
    gui.muted_color               = "#263238"
    gui.hover_muted_color         = "#37474F"
    gui.accent_color              = "#00E5FF"
    gui.focus_color               = "#0277BD"

    # Perbaikan error runtime aset frame yang hilang (menggunakan Solid bertema Dark Tech)
    gui.frame_background          = Solid("#0F192AEE")
    gui.confirm_frame_background  = Solid("#0D1B2A")

## ─── TEXTBOX (Dialog Box) ─────────────────────────────────────

## Override warna textbox agar lebih dark & premium
style default:
    font "DejaVuSans.ttf"
    size 22

style say_dialogue:
    size 20
    color "#E8F5E9"
    outlines [(1, "#000000", 0, 0)]

style say_thought:
    size 20
    color "#B3E5FC"
    italic True

style say_label:
    size 22
    bold True
    outlines [(2, "#000000AA", 1, 1)]

## ─── LAYAR MENU PILIHAN (Choice) ─────────────────────────────
## Mengatur tampilan tombol pilihan (menu) saat pemain harus memilih opsi.

style choice_vbox:
    spacing 12 # Jarak antar tombol pilihan

style choice_button:
    background Frame("#0D1B2A", 6, 6) # Latar tombol saat diam
    hover_background Frame("#0D3B5E", 6, 6) # Latar tombol saat kursor di atasnya
    selected_background Frame("#0D2E4D", 6, 6) # Latar tombol saat dipilih
    padding (20, 12)
    xminimum 560
    xalign 0.5

style choice_button_text:
    color "#90CAF9"
    hover_color "#00E5FF"
    size 18
    xalign 0.5

## ─── QUICK MENU KUSTOM ────────────────────────────────────────

style quick_button:
    background None
    hover_background None
    padding (6, 4)

style quick_button_text:
    size 14
    color "#546E7A"
    hover_color "#00E5FF"
    outlines []

## ─── OVERRIDE KHUSUS ANDROID (variant small) ─────────────────
## Memastikan ukuran teks dan tombol nyaman untuk layar sentuh Android.

style say_dialogue is default:
    variant "small"
    size 42
    color "#E8F5E9"
    outlines [(2, "#000000", 0, 0)]

style say_thought is say_dialogue:
    variant "small"
    size 42
    color "#B3E5FC"
    italic True

style say_label is default:
    variant "small"
    size 50
    bold True
    outlines [(2, "#000000AA", 1, 1)]

style choice_vbox:
    variant "small"
    spacing 18

style choice_button:
    variant "small"
    background Frame("#0D1B2A", 6, 6)
    hover_background Frame("#0D3B5E", 6, 6)
    selected_background Frame("#0D2E4D", 6, 6)
    padding (30, 18)
    xminimum 800
    xalign 0.5

style choice_button_text:
    variant "small"
    color "#90CAF9"
    hover_color "#00E5FF"
    size 40
    xalign 0.5

style quick_button:
    variant "small"
    background None
    hover_background None
    padding (18, 12)

style quick_button_text:
    variant "small"
    size 38
    color "#78909C"
    hover_color "#00E5FF"
    outlines []

## ─── LAYAR SPLASH / TITLE ─────────────────────────────────────

screen splash_tkj():
    """Layar splash intro sebelum menu utama."""
    modal True

    frame:
        background "#000000"
        xfill True
        yfill True

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "⚙  NETPRO" size 56 color "#00E5FF" bold True xalign 0.5
            text "Magang Jaringan" size 28 color "#B0BEC5" xalign 0.5
            null height 10
            text "Visual Novel Edukasi TKJ" size 16 color "#546E7A" xalign 0.5
            null height 30

            textbutton "▶  MULAI PETUALANGAN":
                xalign 0.5
                action Hide("splash_tkj")
                background Frame("#0D3B5E", 10, 10)
                hover_background Frame("#0277BD", 10, 10)
                padding (28, 14)
                text_color "#E3F2FD"
                text_hover_color "#00E5FF"
                text_size 18
                text_bold True

## ─── STYLE UNTUK SISTEM MONITOR (HUD) ───────────────────────

style hud_frame:
    background Frame("#12192BAA", 8, 8)
    padding (14, 10)

style hud_text:
    size 14
    color "#90CAF9"

## ─── TOOLTIP / INFO PANELS ───────────────────────────────────

screen info_panel(judul, isi):
    """Panel informasi eduktif floating."""
    frame:
        xalign 0.5
        yalign 0.1
        background Frame("#0D1B2A", 10, 10)
        padding (16, 12)
        vbox:
            spacing 6
            text "ℹ  [judul]" size 14 color "#00E5FF" bold True
            text isi size 13 color "#B0BEC5"

## ─── GAME MENU OVERLAY (Settings, Save, Load, dll) ──────────

## Hapus transparansi agar teks terbaca jelas di semua layar menu
style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "#000000CC"

style game_menu_navigation_frame:
    xsize 420
    yfill True
    background "#0D1117EE"

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15
    background "#0F192AEE"

## ─── POPUP DIAGRAM LOOP SWITCH (BROADCAST STORM) ───────────

init python:
    class SwitchLoopCanvas(renpy.Displayable):
        def __init__(self, **kwargs):
            super(SwitchLoopCanvas, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            canvas = r.canvas()
            
            # Colors in RGB format (safe for all Pygame versions in Ren'Py)
            red_cable = (255, 82, 82)
            yellow_cable = (255, 215, 0)
            
            # Draw red cables (ring topology)
            canvas.line(red_cable, (230, 180), (400, 60), 5)
            canvas.line(red_cable, (400, 60), (570, 180), 5)
            canvas.line(red_cable, (570, 180), (510, 360), 5)
            canvas.line(red_cable, (510, 360), (290, 360), 5)
            canvas.line(red_cable, (290, 360), (230, 180), 5)
            
            # Draw yellow loop cable (redundant path causing storm)
            canvas.line(yellow_cable, (290, 360), (570, 180), 8)
            
            return r

        def event(self, ev, x, y, st):
            pass

        def visit(self):
            return []

screen diagram_broadcast_storm():
    modal True
    
    # Dark overlay background
    add Solid("#000000B3")
    
    # Diagram Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 720
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (25, 20)
            xfill True
            yfill True
            
            vbox:
                spacing 15
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM DIAGNOSTIK TOPOLOGI // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "BROADCAST STORM & STP DIAGRAM" size 28 color "#E3F2FD" bold True xalign 0.5
                
                # Canvas container for absolute positioning of Switch elements
                fixed:
                    xsize 800
                    ysize 450
                    xalign 0.5
                    
                    # 1. Custom canvas drawing cables
                    add SwitchLoopCanvas()
                    
                    # 2. Top Switch
                    frame:
                        xpos 400 ypos 60 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (20, 10)
                            text "SW" size 16 color "#E3F2FD" bold True xalign 0.5 yalign 0.5
                            
                    # 3. Top-Left Switch
                    frame:
                        xpos 230 ypos 180 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (20, 10)
                            text "SW" size 16 color "#E3F2FD" bold True xalign 0.5 yalign 0.5
                            
                    # 4. Top-Right Switch
                    frame:
                        xpos 570 ypos 180 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (20, 10)
                            text "SW" size 16 color "#E3F2FD" bold True xalign 0.5 yalign 0.5
                            
                    # 5. Bottom-Left Switch
                    frame:
                        xpos 290 ypos 360 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (20, 10)
                            text "SW" size 16 color "#E3F2FD" bold True xalign 0.5 yalign 0.5
                            
                    # 6. Bottom-Right Switch
                    frame:
                        xpos 510 ypos 360 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (20, 10)
                            text "SW" size 16 color "#E3F2FD" bold True xalign 0.5 yalign 0.5
                            
                    # 7. Warning "LOOP!" icon in the center of yellow cable
                    frame:
                        xpos 430 ypos 270 anchor (0.5, 0.5)
                        background Solid("#FF5252")
                        padding (12, 6)
                        hbox:
                            spacing 5
                            text "⚠️ LOOP!" size 16 color "#FFFFFF" bold True xalign 0.5 yalign 0.5
                            
                # Bottom Concept Panel
                frame:
                    background Solid("#1E293B")
                    xalign 0.5
                    xsize 780
                    padding (15, 12)
                    vbox:
                        xalign 0.5
                        spacing 4
                        text "Status: ❌ LOOP TOPOLOGI TERDETEKSI (Kabel Kuning)" size 14 color "#FF5252" bold True xalign 0.5
                        text "Solusi: Isolasi Port Loop (Cabut Kabel Kuning) + Aktifkan STP" size 16 color "#FFD740" bold True xalign 0.5


## ─── POPUP DIAGRAM VLAN & SUBNETTING /26 ─────────────────────

init python:
    class VlanTopologyCanvas(renpy.Displayable):
        def __init__(self, **kwargs):
            super(VlanTopologyCanvas, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            canvas = r.canvas()
            
            # RGB Colors
            cyan = (0, 229, 255)
            gold = (255, 215, 0)
            green = (118, 255, 3)
            
            # VLAN 10 (IT) Lines
            canvas.line(cyan, (125, 200), (160, 260), 3)
            canvas.line(cyan, (160, 200), (160, 260), 3)
            canvas.line(cyan, (195, 200), (160, 260), 3)
            
            # VLAN 20 (Marketing) Lines
            canvas.line(gold, (365, 200), (400, 260), 3)
            canvas.line(gold, (400, 200), (400, 260), 3)
            canvas.line(gold, (435, 200), (400, 260), 3)
            
            # VLAN 30 (Finance) Lines
            canvas.line(green, (605, 200), (640, 260), 3)
            canvas.line(green, (640, 200), (640, 260), 3)
            canvas.line(green, (675, 200), (640, 260), 3)
            
            return r

        def event(self, ev, x, y, st):
            pass

        def visit(self):
            return []

screen diagram_vlan_subnetting():
    modal True
    
    # Dark overlay background
    add Solid("#000000B3")
    
    # Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 950
        ysize 720
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (25, 20)
            xfill True
            yfill True
            
            vbox:
                spacing 15
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM SEGMENTASI VLAN & SUBNETTING // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "VLAN & SUBNETTING /26" size 28 color "#E3F2FD" bold True xalign 0.5
                
                # Canvas container for columns and custom lines
                fixed:
                    xsize 800
                    ysize 400
                    xalign 0.5
                    
                    # 1. Background topology lines
                    add VlanTopologyCanvas()
                    
                    # 2. COLUMN 1: VLAN 10 IT (Cyan)
                    frame:
                        xpos 160 ypos 200 anchor (0.5, 0.5)
                        xsize 210
                        ysize 320
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 15)
                            vbox:
                                xalign 0.5
                                spacing 4
                                text "VLAN 10 IT" size 18 color "#00E5FF" bold True xalign 0.5
                                text "192.168.10.0/26" size 12 color "#E3F2FD" xalign 0.5
                                
                    # IT Hosts (little Cyan squares over the lines)
                    frame:
                        xpos 125 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#00E5FF")
                    frame:
                        xpos 160 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#00E5FF")
                    frame:
                        xpos 195 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#00E5FF")
                        
                    # IT Pill (62 HOST)
                    frame:
                        xpos 160 ypos 300 anchor (0.5, 0.5)
                        background Solid("#0F1923")
                        padding (8, 4)
                        xsize 90
                        # 1px border simulation
                        frame:
                            background Solid("#00E5FF")
                            padding (1, 1)
                            frame:
                                background Solid("#0F1923")
                                padding (6, 2)
                                text "62 HOST" size 11 color "#00E5FF" bold True xalign 0.5 yalign 0.5
                                
                    # 3. COLUMN 2: VLAN 20 MARKETING (Gold)
                    frame:
                        xpos 400 ypos 200 anchor (0.5, 0.5)
                        xsize 210
                        ysize 320
                        background Solid("#FFD700")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 15)
                            vbox:
                                xalign 0.5
                                spacing 4
                                text "VLAN 20 MARKETING" size 15 color "#FFD700" bold True xalign 0.5
                                text "192.168.10.64/26" size 12 color "#E3F2FD" xalign 0.5
                                
                    # Marketing Hosts (little Gold squares)
                    frame:
                        xpos 365 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#FFD700")
                    frame:
                        xpos 400 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#FFD700")
                    frame:
                        xpos 435 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#FFD700")
                        
                    # Marketing Pill (62 HOST)
                    frame:
                        xpos 400 ypos 300 anchor (0.5, 0.5)
                        background Solid("#0F1923")
                        padding (8, 4)
                        xsize 90
                        frame:
                            background Solid("#FFD700")
                            padding (1, 1)
                            frame:
                                background Solid("#0F1923")
                                padding (6, 2)
                                text "62 HOST" size 11 color "#FFD700" bold True xalign 0.5 yalign 0.5
                                
                    # 4. COLUMN 3: VLAN 30 FINANCE (Green)
                    frame:
                        xpos 640 ypos 200 anchor (0.5, 0.5)
                        xsize 210
                        ysize 320
                        background Solid("#76FF03")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 15)
                            vbox:
                                xalign 0.5
                                spacing 4
                                text "VLAN 30 FINANCE" size 16 color "#76FF03" bold True xalign 0.5
                                text "192.168.10.128/26" size 12 color "#E3F2FD" xalign 0.5
                                
                    # Finance Hosts (little Green squares)
                    frame:
                        xpos 605 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#76FF03")
                    frame:
                        xpos 640 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#76FF03")
                    frame:
                        xpos 675 ypos 200 anchor (0.5, 0.5)
                        xsize 25 ysize 25
                        background Solid("#76FF03")
                        
                    # Finance Pill (62 HOST)
                    frame:
                        xpos 640 ypos 300 anchor (0.5, 0.5)
                        background Solid("#0F1923")
                        padding (8, 4)
                        xsize 90
                        frame:
                            background Solid("#76FF03")
                            padding (1, 1)
                            frame:
                                background Solid("#0F1923")
                                padding (6, 2)
                                text "62 HOST" size 11 color "#76FF03" bold True xalign 0.5 yalign 0.5
                                
                # Bottom Concept Panel
                frame:
                    background Solid("#1E293B")
                    xalign 0.5
                    xsize 750
                    padding (15, 12)
                    vbox:
                        xalign 0.5
                        spacing 4
                        text "Konsep: Access Port + Trunk + ROAS" size 18 color "#E3F2FD" bold True xalign 0.5


## ─── POPUP DIAGRAM WAN, OSPF, & NAT/PAT ──────────────────────

init python:
    class WanTopologyCanvas(renpy.Displayable):
        def __init__(self, **kwargs):
            super(WanTopologyCanvas, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            canvas = r.canvas()
            
            # Glowing Cyan/Blue Color
            cyan = (0, 229, 255)
            
            # Draw the diamond lines (WAN connections)
            canvas.line(cyan, (200, 220), (400, 70), 5)
            canvas.line(cyan, (400, 70), (600, 220), 5)
            canvas.line(cyan, (200, 220), (400, 370), 5)
            canvas.line(cyan, (600, 220), (400, 370), 5)
            
            return r

        def event(self, ev, x, y, st):
            pass

        def visit(self):
            return []

screen diagram_wan_ospf_nat():
    modal True
    
    # Dark overlay background
    add Solid("#000000B3")
    
    # Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 720
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (25, 20)
            xfill True
            yfill True
            
            vbox:
                spacing 15
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM TOPOLOGI WAN & GATEWAY // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "WAN OSPF + NAT/PAT" size 28 color "#E3F2FD" bold True xalign 0.5
                
                # Canvas container for columns and custom lines
                fixed:
                    xsize 800
                    ysize 420
                    xalign 0.5
                    
                    # 1. Background OSPF + PAT Topology Lines
                    add WanTopologyCanvas()
                    
                    # 2. ISP Node (Top Node - Gold border)
                    frame:
                        xpos 400 ypos 70 anchor (0.5, 0.5)
                        background Solid("#FFD700")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (25, 10)
                            text "ISP" size 18 color "#E3F2FD" bold True xalign 0.5 yalign 0.5
                            
                    # 3. HQ Router Node (Left Node - Cyan Border Circle)
                    frame:
                        xpos 200 ypos 190 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (12, 12)
                            text "🌀" size 22 xalign 0.5 yalign 0.5
                    text "HQ Router" xpos 200 ypos 240 anchor (0.5, 0.5) size 14 color "#E3F2FD" bold True
                    
                    # 4. Cabang Router Node (Right Node - Cyan Border Circle)
                    frame:
                        xpos 600 ypos 190 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (12, 12)
                            text "🌀" size 22 xalign 0.5 yalign 0.5
                    text "Cabang" xpos 600 ypos 240 anchor (0.5, 0.5) size 14 color "#E3F2FD" bold True
                    
                    # 5. Internet Cloud Node (Bottom Node - Cyan Border Circle)
                    frame:
                        xpos 400 ypos 340 anchor (0.5, 0.5)
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            padding (12, 12)
                            text "☁️" size 22 xalign 0.5 yalign 0.5
                    text "Internet" xpos 400 ypos 390 anchor (0.5, 0.5) size 14 color "#E3F2FD" bold True
                    
                    # 6. Connection Labels (OSPF, PAT, WAN)
                    # Top-Left OSPF Label
                    frame:
                        xpos 290 ypos 120 anchor (0.5, 0.5)
                        background Solid("#0F1923D9")
                        padding (8, 4)
                        text "OSPF" size 12 color "#FFD740" bold True xalign 0.5 yalign 0.5
                        
                    # Top-Right OSPF Label
                    frame:
                        xpos 510 ypos 120 anchor (0.5, 0.5)
                        background Solid("#0F1923D9")
                        padding (8, 4)
                        text "OSPF" size 12 color "#FFD740" bold True xalign 0.5 yalign 0.5
                        
                    # Bottom-Left PAT Label
                    frame:
                        xpos 290 ypos 300 anchor (0.5, 0.5)
                        background Solid("#0F1923D9")
                        padding (8, 4)
                        text "PAT" size 12 color "#00E5FF" bold True xalign 0.5 yalign 0.5
                        
                    # Bottom-Right WAN Label
                    frame:
                        xpos 510 ypos 300 anchor (0.5, 0.5)
                        background Solid("#0F1923D9")
                        padding (8, 4)
                        text "WAN" size 12 color "#00E5FF" bold True xalign 0.5 yalign 0.5
                        
                # Bottom Concept Panel
                frame:
                    background Solid("#1E293B")
                    xalign 0.5
                    xsize 750
                    padding (15, 12)
                    vbox:
                        xalign 0.5
                        spacing 4
                        text "Status: ✅ WAN OSPF & NAT/PAT Aktif" size 14 color "#76FF03" bold True xalign 0.5
                        text "Konsep: NAT overload = banyak IP private memakai 1 IP public" size 16 color "#E3F2FD" bold True xalign 0.5


## ─── POPUP DIAGRAM EXTENDED ACL FIREWALL ────────────────────

init python:
    class AclTopologyCanvas(renpy.Displayable):
        def __init__(self, **kwargs):
            super(AclTopologyCanvas, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            canvas = r.canvas()
            
            # RGB Colors
            red_line = (255, 82, 82)
            green_line = (118, 255, 3)
            
            # Draw the horizontal lines (Telnet vs Traffic Aman)
            canvas.line(red_line, (200, 200), (400, 200), 5)
            canvas.line(green_line, (400, 200), (600, 200), 5)
            
            return r

        def event(self, ev, x, y, st):
            pass

        def visit(self):
            return []

screen diagram_extended_acl():
    modal True
    
    # Dark overlay background
    add Solid("#000000B3")
    
    # Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 720
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (25, 20)
            xfill True
            yfill True
            
            vbox:
                spacing 15
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM KEAMANAN JARINGAN // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "EXTENDED ACL FIREWALL" size 28 color "#E3F2FD" bold True xalign 0.5
                
                # Canvas container for columns and custom lines
                fixed:
                    xsize 800
                    ysize 420
                    xalign 0.5
                    
                    # 1. Background ACL Topology Lines
                    add AclTopologyCanvas()
                    
                    # 2. Attacker Node (Left Node - Red border)
                    frame:
                        xpos 200 ypos 200 anchor (0.5, 0.5)
                        xsize 150
                        ysize 120
                        background Solid("#FF5252")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 10)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 8
                                text "💀" size 26 xalign 0.5
                                text "ATTACKER" size 14 color "#FF5252" bold True xalign 0.5
                                
                    # 3. Firewall Node (Center Node - Gold border)
                    frame:
                        xpos 400 ypos 200 anchor (0.5, 0.5)
                        xsize 170
                        ysize 150
                        background Solid("#FFD700")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 10)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 4
                                text "FIREWALL" size 15 color "#FFD700" bold True xalign 0.5
                                text "🛡️" size 22 xalign 0.5
                                text "deny tcp any host" size 10 color "#FF5252" bold True xalign 0.5
                                text "server eq 23" size 10 color "#FF5252" bold True xalign 0.5
                                
                    # 4. DB Server Node (Right Node - Green border)
                    frame:
                        xpos 600 ypos 200 anchor (0.5, 0.5)
                        xsize 150
                        ysize 120
                        background Solid("#76FF03")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 10)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 8
                                text "🗄️" size 26 xalign 0.5
                                text "DB SERVER" size 14 color "#76FF03" bold True xalign 0.5
                                
                    # 5. Connection Labels
                    # Attacker -> Firewall: Red Label "Telnet 23"
                    frame:
                        xpos 300 ypos 175 anchor (0.5, 0.5)
                        background Solid("#0F1923D9")
                        padding (8, 4)
                        text "Telnet 23" size 12 color "#FF5252" bold True xalign 0.5 yalign 0.5
                        
                    # Firewall -> DB Server: Green Label "traffic aman"
                    frame:
                        xpos 500 ypos 175 anchor (0.5, 0.5)
                        background Solid("#0F1923D9")
                        padding (8, 4)
                        text "traffic aman" size 12 color "#76FF03" bold True xalign 0.5 yalign 0.5
                        
                # Bottom Concept Panel
                frame:
                    background Solid("#1E293B")
                    xalign 0.5
                    xsize 750
                    padding (15, 12)
                    vbox:
                        xalign 0.5
                        spacing 4
                        text "Status: 🛡️ ATTACK BLOCK BY EXTENDED ACL" size 14 color "#76FF03" bold True xalign 0.5
                        text "Konsep: Blokir Telnet/port 23 dari internet ke server internal." size 16 color "#E3F2FD" bold True xalign 0.5


## ─── POPUP DIAGRAM TIGA LAYANAN SERVER (DNS, VOIP, PROXY) ─────

screen diagram_three_servers():
    modal True
    
    # Dark overlay background
    add Solid("#000000B3")
    
    # Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 950
        ysize 720
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (25, 20)
            xfill True
            yfill True
            
            vbox:
                spacing 15
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM LAYANAN APLIKASI // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "DNS, VoIP & PROXY SERVER" size 28 color "#E3F2FD" bold True xalign 0.5
                
                # Canvas container for cards
                fixed:
                    xsize 800
                    ysize 400
                    xalign 0.5
                    
                    # 1. COLUMN 1: DNS BIND9 (Cyan)
                    frame:
                        xpos 160 ypos 200 anchor (0.5, 0.5)
                        xsize 210
                        ysize 320
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 15)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 10
                                text "🖥️" size 42 color "#00E5FF" xalign 0.5
                                text "DNS BIND9" size 18 color "#00E5FF" bold True xalign 0.5
                                text "absen.nusanet.local" size 12 color "#E3F2FD" xalign 0.5
                                
                    # 2. COLUMN 2: VoIP Asterisk (Green)
                    frame:
                        xpos 400 ypos 200 anchor (0.5, 0.5)
                        xsize 210
                        ysize 320
                        background Solid("#76FF03")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 15)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 10
                                text "🖥️" size 42 color "#76FF03" xalign 0.5
                                text "VoIP Asterisk" size 18 color "#76FF03" bold True xalign 0.5
                                text "SIP extensions" size 12 color "#E3F2FD" xalign 0.5
                                
                    # 3. COLUMN 3: Squid Proxy (Red)
                    frame:
                        xpos 640 ypos 200 anchor (0.5, 0.5)
                        xsize 210
                        ysize 320
                        background Solid("#FF5252")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 15)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 10
                                text "🖥️" size 42 color "#FF5252" xalign 0.5
                                text "Squid Proxy" size 18 color "#FF5252" bold True xalign 0.5
                                text "deny dst-domain" size 12 color "#E3F2FD" xalign 0.5
                                
                # Bottom Concept Panel
                frame:
                    background Solid("#1E293B")
                    xalign 0.5
                    xsize 750
                    padding (15, 12)
                    vbox:
                        xalign 0.5
                        spacing 4
                        text "Status: 🌐 LAYANAN SERVER AKTIF & BERFUNGSI" size 14 color "#76FF03" bold True xalign 0.5
                        text "Layer 7: layanan aplikasi yang langsung dirasakan user" size 16 color "#E3F2FD" bold True xalign 0.5


## ─── POPUP DIAGRAM QOS, VPN, & DISASTER RECOVERY ────────────

screen diagram_qos_vpn_dr():
    modal True
    
    # Dark overlay background
    add Solid("#000000B3")
    
    # Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 950
        ysize 720
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (25, 20)
            xfill True
            yfill True
            
            vbox:
                spacing 15
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM MANAJEMEN & PENANGGULANGAN BENCANA // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "QOS, VPN & DISASTER RECOVERY" size 28 color "#E3F2FD" bold True xalign 0.5
                
                # Container for 2x2 grid
                fixed:
                    xsize 800
                    ysize 400
                    xalign 0.5
                    
                    # Row 1, Left Card: QoS Simple Queue (Cyan)
                    frame:
                        xpos 210 ypos 100 anchor (0.5, 0.5)
                        xsize 360
                        ysize 130
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 10)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 6
                                text "QoS Simple Queue" size 18 color "#00E5FF" bold True xalign 0.5
                                text "Prioritas Zoom CEO" size 14 color "#E3F2FD" xalign 0.5
                                
                    # Row 1, Right Card: VPN L2TP/IPSec (Gold)
                    frame:
                        xpos 590 ypos 100 anchor (0.5, 0.5)
                        xsize 360
                        ysize 130
                        background Solid("#FFD700")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 10)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 6
                                text "VPN L2TP/IPSec" size 18 color "#FFD700" bold True xalign 0.5
                                text "Akses aman remote" size 14 color "#E3F2FD" xalign 0.5
                                
                    # Row 2, Left Card: Ransomware Containment (Red)
                    frame:
                        xpos 210 ypos 250 anchor (0.5, 0.5)
                        xsize 360
                        ysize 130
                        background Solid("#FF5252")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 10)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 6
                                text "Ransomware Containment" size 18 color "#FF5252" bold True xalign 0.5
                                text "Cabut LAN terinfeksi" size 14 color "#E3F2FD" xalign 0.5
                                
                    # Row 2, Right Card: Backup Restore (Green)
                    frame:
                        xpos 590 ypos 250 anchor (0.5, 0.5)
                        xsize 360
                        ysize 130
                        background Solid("#76FF03")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (10, 10)
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 6
                                text "Backup Restore" size 18 color "#76FF03" bold True xalign 0.5
                                text "Pulihkan config .rsc" size 14 color "#E3F2FD" xalign 0.5
                                
                # Bottom Concept Panel
                frame:
                    background Solid("#1E293B")
                    xalign 0.5
                    xsize 750
                    padding (15, 12)
                    vbox:
                        xalign 0.5
                        spacing 4
                        text "QoS menjaga prioritas koneksi, VPN untuk akses aman," size 15 color "#E3F2FD" bold True xalign 0.5
                        text "backup untuk pemulihan cepat." size 15 color "#E3F2FD" bold True xalign 0.5


## ─── POPUP DIAGRAM QUIZ REFLEKSI & SKOR ──────────────────────

screen diagram_quiz_skor():
    modal True
    
    # Dark overlay background
    add Solid("#000000B3")
    
    # Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 720
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (25, 20)
            xfill True
            yfill True
            
            vbox:
                spacing 15
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM EVALUASI AKHIR // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "QUIZ REFLEKSI & SKOR" size 28 color "#E3F2FD" bold True xalign 0.5
                
                # Container for elements
                fixed:
                    xsize 800
                    ysize 400
                    xalign 0.5
                    
                    # 1. Example Card at the Top
                    frame:
                        xpos 400 ypos 70 anchor (0.5, 0.5)
                        xsize 760
                        ysize 100
                        background Solid("#78909C")
                        padding (2, 2)
                        frame:
                            background Solid("#0F1923")
                            xfill True
                            yfill True
                            padding (15, 12)
                            vbox:
                                spacing 6
                                text "Contoh: Jumlah host valid pada subnet /26?" size 16 color "#E3F2FD" bold True
                                text "Jawaban benar: 62 Host • Bonus +10 poin" size 14 color "#76FF03" bold True
                                
                    # 2. Row 1: Quest Utama (Cyan bar)
                    text "Quest Utama" xpos 100 ypos 180 anchor (0.0, 0.5) size 16 color "#E3F2FD" bold True
                    # Background Bar
                    frame:
                        xpos 280 ypos 180 anchor (0.0, 0.5)
                        xsize 380 ysize 22
                        background Solid("#00E5FF")
                        padding (2, 2)
                        frame:
                            background Solid("#000000")
                            xfill True
                            yfill True
                            padding (0, 0)
                            # Filled Part (80%)
                            frame:
                                xalign 0.0
                                xsize 300 # 376 * 0.8 = 300
                                ysize 18
                                background Solid("#00E5FF")
                    text "80" xpos 690 ypos 180 anchor (0.0, 0.5) size 18 color "#00E5FF" bold True
                    
                    # 3. Row 2: Insiden Klimaks (Gold bar)
                    text "Insiden Klimaks" xpos 100 ypos 240 anchor (0.0, 0.5) size 16 color "#E3F2FD" bold True
                    # Background Bar
                    frame:
                        xpos 280 ypos 240 anchor (0.0, 0.5)
                        xsize 380 ysize 22
                        background Solid("#FFD700")
                        padding (2, 2)
                        frame:
                            background Solid("#000000")
                            xfill True
                            yfill True
                            padding (0, 0)
                            # Filled Part (70%)
                            frame:
                                xalign 0.0
                                xsize 263 # 376 * 0.7 = 263
                                ysize 18
                                background Solid("#FFD700")
                    text "70" xpos 690 ypos 240 anchor (0.0, 0.5) size 18 color "#FFD700" bold True
                    
                    # 4. Row 3: Kuis Refleksi (Green bar)
                    text "Kuis Refleksi" xpos 100 ypos 300 anchor (0.0, 0.5) size 16 color "#E3F2FD" bold True
                    # Background Bar
                    frame:
                        xpos 280 ypos 300 anchor (0.0, 0.5)
                        xsize 380 ysize 22
                        background Solid("#76FF03")
                        padding (2, 2)
                        frame:
                            background Solid("#000000")
                            xfill True
                            yfill True
                            padding (0, 0)
                            # Filled Part (90%)
                            frame:
                                xalign 0.0
                                xsize 338 # 376 * 0.9 = 338
                                ysize 18
                                background Solid("#76FF03")
                    text "90" xpos 690 ypos 300 anchor (0.0, 0.5) size 18 color "#76FF03" bold True
                    
                # Bottom Concept Panel
                frame:
                    background Solid("#1E293B")
                    xalign 0.5
                    xsize 750
                    padding (15, 12)
                    vbox:
                        xalign 0.5
                        spacing 4
                        text "Skor membantu pemain memahami hasil belajar dan progres penyelesaian misi." size 15 color "#E3F2FD" bold True xalign 0.5


## ─── POPUP DIAGRAM 3 ENDING EVALUASI ─────────────────────────

screen diagram_ending_evaluasi(ending_type, final_score):
    modal True
    
    # Dark overlay background
    add Solid("#000000D0")
    
    # Main Window Panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1150
        ysize 880
        background Frame(Solid("#0A0D14"), 10, 10)
        padding (3, 3)
        
        frame:
            background Solid("#0F1923")
            padding (30, 25)
            xfill True
            yfill True
            
            vbox:
                spacing 20
                xfill True
                yfill True
                
                # Header Panel
                hbox:
                    xfill True
                    text "DIAGRAM EVALUASI AKHIR MAGANG // NETPRO" size 14 color "#00E5FF" bold True xalign 0.0
                    textbutton "❌ [[ TUTUP ]]" action Return():
                        text_size 14
                        text_color "#FF5252"
                        text_hover_color "#FFD740"
                        background None
                        
                text "3 ENDING EVALUASI KINERJA" size 30 color "#E3F2FD" bold True xalign 0.5
                
                # Cards Container
                hbox:
                    spacing 30
                    xalign 0.5
                    
                    # CARD 1: TEKNISI PRO (Green, >= 70)
                    $ is_pro = (ending_type == "pro")
                    $ pro_border = "#76FF03" if is_pro else "#263238"
                    $ pro_bg = "#0F1923" if is_pro else "#080B0F"
                    $ pro_text = "#E3F2FD" if is_pro else "#455A64"
                    $ pro_title = "#76FF03" if is_pro else "#2E4F02"
                    
                    frame:
                        xsize 320
                        ysize 400
                        background Solid(pro_border)
                        padding (2, 2)
                        frame:
                            background Solid(pro_bg)
                            xfill True
                            yfill True
                            padding (20, 20)
                            vbox:
                                spacing 15
                                xfill True
                                yfill True
                                
                                text ">= 70" size 38 color pro_title bold True xalign 0.5
                                text "TEKNISI PRO" size 22 color pro_text bold True xalign 0.5
                                text "Diterima kerja tetap" size 16 color pro_text xalign 0.5 text_align 0.5
                                
                                null height 10
                                # Divider
                                frame:
                                    ysize 2
                                    background Solid(pro_border)
                                    xfill True
                                null height 10
                                
                                text "Pak Admin dan Pak Hendra menilai rapor akhir." size 13 color pro_text xalign 0.5 text_align 0.5
                                
                                if is_pro:
                                    text "🏆 SELESAI" size 14 color "#76FF03" bold True xalign 0.5
                                    
                    # CARD 2: PENGEMBANGAN (Gold, 40-69)
                    $ is_mid = (ending_type == "mid")
                    $ mid_border = "#FFD700" if is_mid else "#263238"
                    $ mid_bg = "#0F1923" if is_mid else "#080B0F"
                    $ mid_text = "#E3F2FD" if is_mid else "#455A64"
                    $ mid_title = "#FFD700" if is_mid else "#5A4C00"
                    
                    frame:
                        xsize 320
                        ysize 400
                        background Solid(mid_border)
                        padding (2, 2)
                        frame:
                            background Solid(mid_bg)
                            xfill True
                            yfill True
                            padding (20, 20)
                            vbox:
                                spacing 15
                                xfill True
                                yfill True
                                
                                text "40-69" size 38 color mid_title bold True xalign 0.5
                                text "PENGEMBANGAN" size 20 color mid_text bold True xalign 0.5
                                text "Perpanjangan magang" size 16 color mid_text xalign 0.5 text_align 0.5
                                
                                null height 10
                                # Divider
                                frame:
                                    ysize 2
                                    background Solid(mid_border)
                                    xfill True
                                null height 10
                                
                                text "Pak Admin dan Pak Hendra menilai rapor akhir." size 13 color mid_text xalign 0.5 text_align 0.5
                                
                                if is_mid:
                                    text "🔄 SELESAI" size 14 color "#FFD700" bold True xalign 0.5

                    # CARD 3: BELAJAR LAGI (Red, < 40)
                    $ is_bad = (ending_type == "bad")
                    $ bad_border = "#FF5252" if is_bad else "#263238"
                    $ bad_bg = "#0F1923" if is_bad else "#080B0F"
                    $ bad_text = "#E3F2FD" if is_bad else "#455A64"
                    $ bad_title = "#FF5252" if is_bad else "#5A1C1C"
                    
                    frame:
                        xsize 320
                        ysize 400
                        background Solid(bad_border)
                        padding (2, 2)
                        frame:
                            background Solid(bad_bg)
                            xfill True
                            yfill True
                            padding (20, 20)
                            vbox:
                                spacing 15
                                xfill True
                                yfill True
                                
                                text "< 40" size 38 color bad_title bold True xalign 0.5
                                text "BELAJAR LAGI" size 22 color bad_text bold True xalign 0.5
                                text "Ulangi materi dasar" size 16 color bad_text xalign 0.5 text_align 0.5
                                
                                null height 10
                                # Divider
                                frame:
                                    ysize 2
                                    background Solid(bad_border)
                                    xfill True
                                null height 10
                                
                                text "Pak Admin dan Pak Hendra menilai rapor akhir." size 13 color bad_text xalign 0.5 text_align 0.5
                                
                                if is_bad:
                                    text "💪 SELESAI" size 14 color "#FF5252" bold True xalign 0.5
                                    
                null height 15
                
                # Feedback Message Box
                $ msg_title = ""
                $ msg_body = ""
                $ msg_color = "#00E5FF"
                
                if ending_type == "pro":
                    $ msg_title = "SELAMAT! ANDA LULUS SEBAGAI TEKNISI PRO 🏆"
                    $ msg_body = "Luar biasa! Dengan total skor [final_score] poin, Anda membuktikan kompetensi setara Teknisi Senior. Anda resmi direkrut sebagai Junior Network Engineer Full-Time di PT. Nusanet Teknologi! Tetaplah berinovasi dan pertahankan semangat belajarmu!"
                    $ msg_color = "#76FF03"
                elif ending_type == "mid":
                    $ msg_title = "TETAP SEMANGAT: PROGRAM PENGEMBANGAN 🔄"
                    $ msg_body = "Kerja bagus! Total skor Anda: [final_score] poin. Anda menunjukkan pemahaman dasar yang solid. Untuk mempersiapkan Anda menghadapi industri secara nyata, Anda berhak atas perpanjangan magang selama 3 bulan untuk mempertajam keahlian Cisco & Mikrotik!"
                    $ msg_color = "#FFD700"
                else:
                    $ msg_title = "AYO MULAI LAGI: BELAJAR LEBIH GIAT 💪"
                    $ msg_body = "Total skor Anda: [final_score] poin. Jangan berkecil hati, kegagalan adalah awal dari keahlian sejati. Pelajari kembali konsep crimping kabel, routing dasar, dan IP subnetting /26. Kami percaya Anda bisa berhasil di percobaan berikutnya!"
                    $ msg_color = "#FF5252"
                
                frame:
                    background Solid("#12192B")
                    xalign 0.5
                    xsize 1020
                    ysize 160
                    padding (2, 2)
                    frame:
                        background Solid("#0F1923")
                        xfill True
                        yfill True
                        padding (15, 12)
                        vbox:
                            spacing 6
                            text "[msg_title]" size 16 color msg_color bold True xalign 0.5
                            text "[msg_body]" size 14 color "#E3F2FD" xalign 0.5 text_align 0.5 line_spacing 4
                            
                null height 10
                
                # Navigation Action Button
                textbutton "LANJUTKAN KE LAPORAN AKHIR" action Return():
                    xalign 0.5
                    background Frame("#0D3B5E", 10, 10)
                    hover_background Frame("#0277BD", 10, 10)
                    padding (20, 10)
                    text_color "#E3F2FD"
                    text_hover_color "#00E5FF"
                    text_size 16
                    text_bold True
