import sublime, sublime_plugin

class SelectAndCopyCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command("find_under_expand")
    self.window.run_command("markSelection")
    self.window.run_command("copy")

class SelectAndPasteCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command("find_under_expand")
    self.window.run_command("markSelection")
    self.window.run_command("paste")