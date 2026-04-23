## ============================================================
## gui_custom.rpy — Kustomisasi UI Premium untuk NetPro TKJ
## ============================================================

## ─── WARNA TEMA UTAMA ─────────────────────────────────────────

## Dark tech palette
define ACCENT_BLUE    = "#00E5FF"
define ACCENT_GOLD    = "#FFD700"
define DARK_BG        = "#0D1117"
define PANEL_BG       = "#0F1923"
define TEXT_PRIMARY   = "#E3F2FD"
define TEXT_MUTED     = "#78909C"
define SUCCESS_COLOR  = "#76FF03"
define WARNING_COLOR  = "#FFD740"
define DANGER_COLOR   = "#FF5252"

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

style choice_vbox:
    spacing 12

style choice_button:
    background Frame("#0D1B2A", 6, 6)
    hover_background Frame("#0D3B5E", 6, 6)
    selected_background Frame("#0D2E4D", 6, 6)
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
