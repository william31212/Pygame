from imgui_pygame_intergation import PygameRenderer
import imgui

class dbg_view:
	def __init__(self, size):
		io = imgui.get_io()
		io.fonts.add_font_default()
		io.display_size = size

		self.renderer = PygameRenderer()

	def update(self):
		imgui.new_frame()

	def render(self):
		imgui.render()

	def handle_event(self, e):
		self.renderer.process_event(e)