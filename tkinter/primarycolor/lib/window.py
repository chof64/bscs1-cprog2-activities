
def window_geometry(context):
    window_width = 600
    window_height = 300
    screen_width = context.winfo_screenwidth()
    screen_height = context.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    return f"{window_width}x{window_height}+{x}+{y}"
