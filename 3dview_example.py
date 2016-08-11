from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Mesh, RenderContext, Color, Callback
from kivy.graphics.opengl import glDisable, glEnable, GL_DEPTH_TEST
from kivy.graphics.transformation import Matrix
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

vs3d = '''
#ifdef GL_ES
    precision highp float;
#endif
/* Outputs to the fragment shader */
varying vec4 frag_color;
varying vec2 tex_coord0;
/* vertex attributes */
attribute vec3     vPosition;
attribute vec4     vColor;
attribute vec2     vTexCoords0;
/* uniform variables */
uniform mat4       modelview_mat;
uniform mat4       projection_mat;
uniform vec4       color;
void main (void) {
  frag_color = color * vColor;
  tex_coord0 = vTexCoords0;
  gl_Position = projection_mat * modelview_mat * vec4(vPosition.xyz, 1.0);
}
'''

Builder.load_string('''
<ViewControler>:
    GridLayout:
        size_hint_x: .2
        cols: 2
        Label:
            text: 'fovy'
        Slider:
            value: 45.
            on_value: root.view.params['fovy'] = args[1]
        Label:
            text: 'aspect'
        Slider:
            value: 1.
            max: 2.
            on_value: root.view.params['aspect'] = args[1]
        Label:
            text: 'zNear'
        Slider:
            value: 0.1
            min: 1
            max: 10
            on_value: root.view.params['zNear'] = args[1]
        Label:
            text: 'zMax'
        Slider:
            value: 1000.
            min: 100
            max: 1000
            on_value: root.view.params['zFar'] = args[1]
''')

class ViewControler(FloatLayout):
    view = ObjectProperty(None)

class View3D(FloatLayout):
    def __init__(self, **kwargs):
        self.params = {}
        self.canvas = RenderContext()
        self.canvas.shader.vs = vs3d
        self.targetx = 0
        self.targety = 0
        super(View3D, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_glsl, 0)

        with self.canvas:
            Callback(self.activate_depthtest)
            Color(.8, 0, .7)
            self.create_3dcube(pos=(0, 0, 0), size=(100, 100, 100))
            Callback(self.deactivate_depthtest)

    def activate_depthtest(self, instr):
        glEnable(GL_DEPTH_TEST)

    def deactivate_depthtest(self, instr):
        glDisable(GL_DEPTH_TEST)

    def create_3dcube(self, pos, size):
        x, y, z = pos
        w, h, p = size
        fmt = [('vPosition', 3, 'float'), ('vColor', 4, 'float')]
        vertices = [
            x, y, z, 1, 0, 0, 1,
            x + w, y, z, .5, .5, 0, 1,
            x + w, y + h, z, 0, 1, 0, 1,
            x, y + h, z, 0, .5, .5, 1,
            x, y, z + p, 0, 0, 1, 1,
            x + w, y, z + p, .5, 0, .5, 1,
            x + w, y + h, z + p, 0, 0, 0, 1,
            x, y + h, z + p, 1, 1, 1, 1 ]
        indices = [
            0, 2, 1,
            0, 3, 2,
            5, 0, 1,
            5, 4, 0,
            5, 2, 6,
            5, 1, 2,
            4, 3, 0,
            4, 7, 3,
            2, 7, 6,
            2, 3, 7,
            5, 6, 4,
            4, 6, 7]

        Color(1, 1, 1)
        Mesh(vertices=vertices, indices=indices, fmt=fmt, mode='triangles')

        vertices = [
            x, y, z, 1, 1, 1, 1,
            x + w, y, z, 1, 1, 1, 1,
            x + w, y + h, z, 1, 1, 1, 1,
            x, y + h, z, 1, 1, 1, 1,
            x, y, z + p, 1, 1, 1, 1,
            x + w, y, z + p, 1, 1, 1, 1,
            x + w, y + h, z + p, 1, 1, 1, 1,
            x, y + h, z + p, 1, 1, 1, 1]
        indices = [
            0, 2, 2, 1, 1, 0, 0, 3, 3, 2,
            1, 5, 2, 5, 2, 6, 6, 5,
            0, 4, 4, 3, 3, 7, 7, 4,
            7, 2, 0, 5, 4, 5, 7, 6, 4, 6]

        Color(1, 1, 1)
        Mesh(vertices=vertices, indices=indices, fmt=fmt, mode='lines')

    def update_glsl(self, dt):
        from kivy.core.window import Window
        g = self.params.get
        w, h = Window.system_size
        projection_mat = Matrix()
        #projection_mat.view_clip(0.0, w, 0.0, h, 10.0, 1000.0, 1)
        projection_mat.perspective(g('fovy', 45.), g('aspect', 1), g('zNear', 10), g('zFar', 1000))
        #projection_mat.view_clip(0.0, w, 0.0, h, -1, 1, 0)
        modelview_mat = Matrix().look_at(0, 200, -200, self.targetx, self.targety, 0, 0, 1, 0)
        self.canvas['projection_mat'] = projection_mat
        self.canvas['modelview_mat'] = modelview_mat

    def on_touch_move(self, touch):
        print touch.dx, touch.dy

        self.targetx -= touch.dx
        self.targety += touch.dy
        return True


class View3DApp(App):
    def build(self):
        root = FloatLayout()
        view3d = View3D()
        root.add_widget(view3d)
        root.add_widget(ViewControler(view=view3d))
        return root

if __name__ == '__main__':
    View3DApp().run()