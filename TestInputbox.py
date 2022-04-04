'Test inputbox from stackoverflow'

import tkinter as tk

root = tk.Tk()
root.wm_geometry("800x600")
dialog = tk.Toplevel(root)
root_name = root.winfo_pathname(root.winfo_id())
dialog_name = dialog.winfo_pathname(dialog.winfo_id())
root.tk.eval('tk::PlaceWindow {0} widget {1}'.format(dialog_name, root_name))
root.mainloop()