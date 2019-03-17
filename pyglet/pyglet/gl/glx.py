# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2018 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------
'''Wrapper for /usr/include/GL/glx.h

Do not modify generated portions of this file.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

from ctypes import *
from pyglet.gl.lib import link_GLX as _link_function
from pyglet.gl.lib import c_ptrdiff_t, c_void

if not _link_function:
    raise ImportError('libGL.so is not available.')

# BEGIN GENERATED CONTENT (do not edit below this line)

# This content is generated by tools/gengl.py.
# Wrapper for /usr/include/GL/glx.h

import pyglet.libs.x11.xlib

# H (/usr/include/GL/glx.h:26)
GLX_VERSION_1_1 = 1 	# /usr/include/GL/glx.h:58
GLX_VERSION_1_2 = 1 	# /usr/include/GL/glx.h:59
GLX_VERSION_1_3 = 1 	# /usr/include/GL/glx.h:60
GLX_VERSION_1_4 = 1 	# /usr/include/GL/glx.h:61
GLX_USE_GL = 1 	# /usr/include/GL/glx.h:70
GLX_BUFFER_SIZE = 2 	# /usr/include/GL/glx.h:71
GLX_LEVEL = 3 	# /usr/include/GL/glx.h:72
GLX_RGBA = 4 	# /usr/include/GL/glx.h:73
GLX_DOUBLEBUFFER = 5 	# /usr/include/GL/glx.h:74
GLX_STEREO = 6 	# /usr/include/GL/glx.h:75
GLX_AUX_BUFFERS = 7 	# /usr/include/GL/glx.h:76
GLX_RED_SIZE = 8 	# /usr/include/GL/glx.h:77
GLX_GREEN_SIZE = 9 	# /usr/include/GL/glx.h:78
GLX_BLUE_SIZE = 10 	# /usr/include/GL/glx.h:79
GLX_ALPHA_SIZE = 11 	# /usr/include/GL/glx.h:80
GLX_DEPTH_SIZE = 12 	# /usr/include/GL/glx.h:81
GLX_STENCIL_SIZE = 13 	# /usr/include/GL/glx.h:82
GLX_ACCUM_RED_SIZE = 14 	# /usr/include/GL/glx.h:83
GLX_ACCUM_GREEN_SIZE = 15 	# /usr/include/GL/glx.h:84
GLX_ACCUM_BLUE_SIZE = 16 	# /usr/include/GL/glx.h:85
GLX_ACCUM_ALPHA_SIZE = 17 	# /usr/include/GL/glx.h:86
GLX_BAD_SCREEN = 1 	# /usr/include/GL/glx.h:92
GLX_BAD_ATTRIBUTE = 2 	# /usr/include/GL/glx.h:93
GLX_NO_EXTENSION = 3 	# /usr/include/GL/glx.h:94
GLX_BAD_VISUAL = 4 	# /usr/include/GL/glx.h:95
GLX_BAD_CONTEXT = 5 	# /usr/include/GL/glx.h:96
GLX_BAD_VALUE = 6 	# /usr/include/GL/glx.h:97
GLX_BAD_ENUM = 7 	# /usr/include/GL/glx.h:98
GLX_VENDOR = 1 	# /usr/include/GL/glx.h:104
GLX_VERSION = 2 	# /usr/include/GL/glx.h:105
GLX_EXTENSIONS = 3 	# /usr/include/GL/glx.h:106
GLX_CONFIG_CAVEAT = 32 	# /usr/include/GL/glx.h:112
GLX_DONT_CARE = 4294967295 	# /usr/include/GL/glx.h:113
GLX_X_VISUAL_TYPE = 34 	# /usr/include/GL/glx.h:114
GLX_TRANSPARENT_TYPE = 35 	# /usr/include/GL/glx.h:115
GLX_TRANSPARENT_INDEX_VALUE = 36 	# /usr/include/GL/glx.h:116
GLX_TRANSPARENT_RED_VALUE = 37 	# /usr/include/GL/glx.h:117
GLX_TRANSPARENT_GREEN_VALUE = 38 	# /usr/include/GL/glx.h:118
GLX_TRANSPARENT_BLUE_VALUE = 39 	# /usr/include/GL/glx.h:119
GLX_TRANSPARENT_ALPHA_VALUE = 40 	# /usr/include/GL/glx.h:120
GLX_WINDOW_BIT = 1 	# /usr/include/GL/glx.h:121
GLX_PIXMAP_BIT = 2 	# /usr/include/GL/glx.h:122
GLX_PBUFFER_BIT = 4 	# /usr/include/GL/glx.h:123
GLX_AUX_BUFFERS_BIT = 16 	# /usr/include/GL/glx.h:124
GLX_FRONT_LEFT_BUFFER_BIT = 1 	# /usr/include/GL/glx.h:125
GLX_FRONT_RIGHT_BUFFER_BIT = 2 	# /usr/include/GL/glx.h:126
GLX_BACK_LEFT_BUFFER_BIT = 4 	# /usr/include/GL/glx.h:127
GLX_BACK_RIGHT_BUFFER_BIT = 8 	# /usr/include/GL/glx.h:128
GLX_DEPTH_BUFFER_BIT = 32 	# /usr/include/GL/glx.h:129
GLX_STENCIL_BUFFER_BIT = 64 	# /usr/include/GL/glx.h:130
GLX_ACCUM_BUFFER_BIT = 128 	# /usr/include/GL/glx.h:131
GLX_NONE = 32768 	# /usr/include/GL/glx.h:132
GLX_SLOW_CONFIG = 32769 	# /usr/include/GL/glx.h:133
GLX_TRUE_COLOR = 32770 	# /usr/include/GL/glx.h:134
GLX_DIRECT_COLOR = 32771 	# /usr/include/GL/glx.h:135
GLX_PSEUDO_COLOR = 32772 	# /usr/include/GL/glx.h:136
GLX_STATIC_COLOR = 32773 	# /usr/include/GL/glx.h:137
GLX_GRAY_SCALE = 32774 	# /usr/include/GL/glx.h:138
GLX_STATIC_GRAY = 32775 	# /usr/include/GL/glx.h:139
GLX_TRANSPARENT_RGB = 32776 	# /usr/include/GL/glx.h:140
GLX_TRANSPARENT_INDEX = 32777 	# /usr/include/GL/glx.h:141
GLX_VISUAL_ID = 32779 	# /usr/include/GL/glx.h:142
GLX_SCREEN = 32780 	# /usr/include/GL/glx.h:143
GLX_NON_CONFORMANT_CONFIG = 32781 	# /usr/include/GL/glx.h:144
GLX_DRAWABLE_TYPE = 32784 	# /usr/include/GL/glx.h:145
GLX_RENDER_TYPE = 32785 	# /usr/include/GL/glx.h:146
GLX_X_RENDERABLE = 32786 	# /usr/include/GL/glx.h:147
GLX_FBCONFIG_ID = 32787 	# /usr/include/GL/glx.h:148
GLX_RGBA_TYPE = 32788 	# /usr/include/GL/glx.h:149
GLX_COLOR_INDEX_TYPE = 32789 	# /usr/include/GL/glx.h:150
GLX_MAX_PBUFFER_WIDTH = 32790 	# /usr/include/GL/glx.h:151
GLX_MAX_PBUFFER_HEIGHT = 32791 	# /usr/include/GL/glx.h:152
GLX_MAX_PBUFFER_PIXELS = 32792 	# /usr/include/GL/glx.h:153
GLX_PRESERVED_CONTENTS = 32795 	# /usr/include/GL/glx.h:154
GLX_LARGEST_PBUFFER = 32796 	# /usr/include/GL/glx.h:155
GLX_WIDTH = 32797 	# /usr/include/GL/glx.h:156
GLX_HEIGHT = 32798 	# /usr/include/GL/glx.h:157
GLX_EVENT_MASK = 32799 	# /usr/include/GL/glx.h:158
GLX_DAMAGED = 32800 	# /usr/include/GL/glx.h:159
GLX_SAVED = 32801 	# /usr/include/GL/glx.h:160
GLX_WINDOW = 32802 	# /usr/include/GL/glx.h:161
GLX_PBUFFER = 32803 	# /usr/include/GL/glx.h:162
GLX_PBUFFER_HEIGHT = 32832 	# /usr/include/GL/glx.h:163
GLX_PBUFFER_WIDTH = 32833 	# /usr/include/GL/glx.h:164
GLX_RGBA_BIT = 1 	# /usr/include/GL/glx.h:165
GLX_COLOR_INDEX_BIT = 2 	# /usr/include/GL/glx.h:166
GLX_PBUFFER_CLOBBER_MASK = 134217728 	# /usr/include/GL/glx.h:167
GLX_SAMPLE_BUFFERS = 100000 	# /usr/include/GL/glx.h:173
GLX_SAMPLES = 100001 	# /usr/include/GL/glx.h:174
class struct___GLXcontextRec(Structure):
    __slots__ = [
    ]
struct___GLXcontextRec._fields_ = [
    ('_opaque_struct', c_int)
]

class struct___GLXcontextRec(Structure):
    __slots__ = [
    ]
struct___GLXcontextRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXContext = POINTER(struct___GLXcontextRec) 	# /usr/include/GL/glx.h:178
XID = pyglet.libs.x11.xlib.XID
GLXPixmap = XID 	# /usr/include/GL/glx.h:179
GLXDrawable = XID 	# /usr/include/GL/glx.h:180
class struct___GLXFBConfigRec(Structure):
    __slots__ = [
    ]
struct___GLXFBConfigRec._fields_ = [
    ('_opaque_struct', c_int)
]

class struct___GLXFBConfigRec(Structure):
    __slots__ = [
    ]
struct___GLXFBConfigRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXFBConfig = POINTER(struct___GLXFBConfigRec) 	# /usr/include/GL/glx.h:182
GLXFBConfigID = XID 	# /usr/include/GL/glx.h:183
GLXContextID = XID 	# /usr/include/GL/glx.h:184
GLXWindow = XID 	# /usr/include/GL/glx.h:185
GLXPbuffer = XID 	# /usr/include/GL/glx.h:186
XVisualInfo = pyglet.libs.x11.xlib.XVisualInfo
Display = pyglet.libs.x11.xlib.Display
# /usr/include/GL/glx.h:190
glXChooseVisual = _link_function('glXChooseVisual', POINTER(XVisualInfo), [POINTER(Display), c_int, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:193
glXCreateContext = _link_function('glXCreateContext', GLXContext, [POINTER(Display), POINTER(XVisualInfo), GLXContext, c_int], 'H')

# /usr/include/GL/glx.h:196
glXDestroyContext = _link_function('glXDestroyContext', None, [POINTER(Display), GLXContext], 'H')

# /usr/include/GL/glx.h:198
glXMakeCurrent = _link_function('glXMakeCurrent', c_int, [POINTER(Display), GLXDrawable, GLXContext], 'H')

# /usr/include/GL/glx.h:201
glXCopyContext = _link_function('glXCopyContext', None, [POINTER(Display), GLXContext, GLXContext, c_ulong], 'H')

# /usr/include/GL/glx.h:204
glXSwapBuffers = _link_function('glXSwapBuffers', None, [POINTER(Display), GLXDrawable], 'H')

Pixmap = pyglet.libs.x11.xlib.Pixmap
# /usr/include/GL/glx.h:206
glXCreateGLXPixmap = _link_function('glXCreateGLXPixmap', GLXPixmap, [POINTER(Display), POINTER(XVisualInfo), Pixmap], 'H')

# /usr/include/GL/glx.h:209
glXDestroyGLXPixmap = _link_function('glXDestroyGLXPixmap', None, [POINTER(Display), GLXPixmap], 'H')

# /usr/include/GL/glx.h:211
glXQueryExtension = _link_function('glXQueryExtension', c_int, [POINTER(Display), POINTER(c_int), POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:213
glXQueryVersion = _link_function('glXQueryVersion', c_int, [POINTER(Display), POINTER(c_int), POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:215
glXIsDirect = _link_function('glXIsDirect', c_int, [POINTER(Display), GLXContext], 'H')

# /usr/include/GL/glx.h:217
glXGetConfig = _link_function('glXGetConfig', c_int, [POINTER(Display), POINTER(XVisualInfo), c_int, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:220
glXGetCurrentContext = _link_function('glXGetCurrentContext', GLXContext, [], 'H')

# /usr/include/GL/glx.h:222
glXGetCurrentDrawable = _link_function('glXGetCurrentDrawable', GLXDrawable, [], 'H')

# /usr/include/GL/glx.h:224
glXWaitGL = _link_function('glXWaitGL', None, [], 'H')

# /usr/include/GL/glx.h:226
glXWaitX = _link_function('glXWaitX', None, [], 'H')

Font = pyglet.libs.x11.xlib.Font
# /usr/include/GL/glx.h:228
glXUseXFont = _link_function('glXUseXFont', None, [Font, c_int, c_int, c_int], 'H')

# /usr/include/GL/glx.h:233
glXQueryExtensionsString = _link_function('glXQueryExtensionsString', c_char_p, [POINTER(Display), c_int], 'H')

# /usr/include/GL/glx.h:235
glXQueryServerString = _link_function('glXQueryServerString', c_char_p, [POINTER(Display), c_int, c_int], 'H')

# /usr/include/GL/glx.h:237
glXGetClientString = _link_function('glXGetClientString', c_char_p, [POINTER(Display), c_int], 'H')

# /usr/include/GL/glx.h:241
glXGetCurrentDisplay = _link_function('glXGetCurrentDisplay', POINTER(Display), [], 'H')

# /usr/include/GL/glx.h:245
glXChooseFBConfig = _link_function('glXChooseFBConfig', POINTER(GLXFBConfig), [POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:248
glXGetFBConfigAttrib = _link_function('glXGetFBConfigAttrib', c_int, [POINTER(Display), GLXFBConfig, c_int, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:251
glXGetFBConfigs = _link_function('glXGetFBConfigs', POINTER(GLXFBConfig), [POINTER(Display), c_int, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:254
glXGetVisualFromFBConfig = _link_function('glXGetVisualFromFBConfig', POINTER(XVisualInfo), [POINTER(Display), GLXFBConfig], 'H')

Window = pyglet.libs.x11.xlib.Window
# /usr/include/GL/glx.h:257
glXCreateWindow = _link_function('glXCreateWindow', GLXWindow, [POINTER(Display), GLXFBConfig, Window, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:260
glXDestroyWindow = _link_function('glXDestroyWindow', None, [POINTER(Display), GLXWindow], 'H')

# /usr/include/GL/glx.h:262
glXCreatePixmap = _link_function('glXCreatePixmap', GLXPixmap, [POINTER(Display), GLXFBConfig, Pixmap, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:265
glXDestroyPixmap = _link_function('glXDestroyPixmap', None, [POINTER(Display), GLXPixmap], 'H')

# /usr/include/GL/glx.h:267
glXCreatePbuffer = _link_function('glXCreatePbuffer', GLXPbuffer, [POINTER(Display), GLXFBConfig, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:270
glXDestroyPbuffer = _link_function('glXDestroyPbuffer', None, [POINTER(Display), GLXPbuffer], 'H')

# /usr/include/GL/glx.h:272
glXQueryDrawable = _link_function('glXQueryDrawable', None, [POINTER(Display), GLXDrawable, c_int, POINTER(c_uint)], 'H')

# /usr/include/GL/glx.h:275
glXCreateNewContext = _link_function('glXCreateNewContext', GLXContext, [POINTER(Display), GLXFBConfig, c_int, GLXContext, c_int], 'H')

# /usr/include/GL/glx.h:279
glXMakeContextCurrent = _link_function('glXMakeContextCurrent', c_int, [POINTER(Display), GLXDrawable, GLXDrawable, GLXContext], 'H')

# /usr/include/GL/glx.h:282
glXGetCurrentReadDrawable = _link_function('glXGetCurrentReadDrawable', GLXDrawable, [], 'H')

# /usr/include/GL/glx.h:284
glXQueryContext = _link_function('glXQueryContext', c_int, [POINTER(Display), GLXContext, c_int, POINTER(c_int)], 'H')

# /usr/include/GL/glx.h:287
glXSelectEvent = _link_function('glXSelectEvent', None, [POINTER(Display), GLXDrawable, c_ulong], 'H')

# /usr/include/GL/glx.h:290
glXGetSelectedEvent = _link_function('glXGetSelectedEvent', None, [POINTER(Display), GLXDrawable, POINTER(c_ulong)], 'H')

PFNGLXGETFBCONFIGSPROC = CFUNCTYPE(POINTER(GLXFBConfig), POINTER(Display), c_int, POINTER(c_int)) 	# /usr/include/GL/glx.h:294
PFNGLXCHOOSEFBCONFIGPROC = CFUNCTYPE(POINTER(GLXFBConfig), POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)) 	# /usr/include/GL/glx.h:295
PFNGLXGETFBCONFIGATTRIBPROC = CFUNCTYPE(c_int, POINTER(Display), GLXFBConfig, c_int, POINTER(c_int)) 	# /usr/include/GL/glx.h:296
PFNGLXGETVISUALFROMFBCONFIGPROC = CFUNCTYPE(POINTER(XVisualInfo), POINTER(Display), GLXFBConfig) 	# /usr/include/GL/glx.h:297
PFNGLXCREATEWINDOWPROC = CFUNCTYPE(GLXWindow, POINTER(Display), GLXFBConfig, Window, POINTER(c_int)) 	# /usr/include/GL/glx.h:298
PFNGLXDESTROYWINDOWPROC = CFUNCTYPE(None, POINTER(Display), GLXWindow) 	# /usr/include/GL/glx.h:299
PFNGLXCREATEPIXMAPPROC = CFUNCTYPE(GLXPixmap, POINTER(Display), GLXFBConfig, Pixmap, POINTER(c_int)) 	# /usr/include/GL/glx.h:300
PFNGLXDESTROYPIXMAPPROC = CFUNCTYPE(None, POINTER(Display), GLXPixmap) 	# /usr/include/GL/glx.h:301
PFNGLXCREATEPBUFFERPROC = CFUNCTYPE(GLXPbuffer, POINTER(Display), GLXFBConfig, POINTER(c_int)) 	# /usr/include/GL/glx.h:302
PFNGLXDESTROYPBUFFERPROC = CFUNCTYPE(None, POINTER(Display), GLXPbuffer) 	# /usr/include/GL/glx.h:303
PFNGLXQUERYDRAWABLEPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int, POINTER(c_uint)) 	# /usr/include/GL/glx.h:304
PFNGLXCREATENEWCONTEXTPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXFBConfig, c_int, GLXContext, c_int) 	# /usr/include/GL/glx.h:305
PFNGLXMAKECONTEXTCURRENTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, GLXDrawable, GLXContext) 	# /usr/include/GL/glx.h:306
PFNGLXGETCURRENTREADDRAWABLEPROC = CFUNCTYPE(GLXDrawable) 	# /usr/include/GL/glx.h:307
PFNGLXGETCURRENTDISPLAYPROC = CFUNCTYPE(POINTER(Display)) 	# /usr/include/GL/glx.h:308
PFNGLXQUERYCONTEXTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXContext, c_int, POINTER(c_int)) 	# /usr/include/GL/glx.h:309
PFNGLXSELECTEVENTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_ulong) 	# /usr/include/GL/glx.h:310
PFNGLXGETSELECTEDEVENTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, POINTER(c_ulong)) 	# /usr/include/GL/glx.h:311
# ARB_get_proc_address (/usr/include/GL/glx.h:317)
GLX_ARB_get_proc_address = 1 	# /usr/include/GL/glx.h:318
__GLXextFuncPtr = CFUNCTYPE(None) 	# /usr/include/GL/glx.h:320
GLubyte = c_ubyte 	# /usr/include/GL/gl.h:160
# /usr/include/GL/glx.h:321
glXGetProcAddressARB = _link_function('glXGetProcAddressARB', __GLXextFuncPtr, [POINTER(GLubyte)], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:328
glXGetProcAddress = _link_function('glXGetProcAddress', POINTER(CFUNCTYPE(None)), [POINTER(GLubyte)], 'ARB_get_proc_address')

PFNGLXGETPROCADDRESSPROC = CFUNCTYPE(__GLXextFuncPtr, POINTER(GLubyte)) 	# /usr/include/GL/glx.h:331
# GLXEXT_LEGACY (/usr/include/GL/glx.h:334)
# VERSION_1_3 (/usr/include/GL/glxext.h:55)
# VERSION_1_4 (/usr/include/GL/glxext.h:114)
# ARB_get_proc_address (/usr/include/GL/glxext.h:119)
# ARB_multisample (/usr/include/GL/glxext.h:122)
# ARB_fbconfig_float (/usr/include/GL/glxext.h:127)
# ARB_create_context (/usr/include/GL/glxext.h:132)
# ARB_create_context_profile (/usr/include/GL/glxext.h:140)
# SGIS_multisample (/usr/include/GL/glxext.h:146)
# EXT_visual_info (/usr/include/GL/glxext.h:151)
# SGI_swap_control (/usr/include/GL/glxext.h:170)
# SGI_video_sync (/usr/include/GL/glxext.h:173)
# SGI_make_current_read (/usr/include/GL/glxext.h:176)
# SGIX_video_source (/usr/include/GL/glxext.h:179)
# EXT_visual_rating (/usr/include/GL/glxext.h:182)
# EXT_import_context (/usr/include/GL/glxext.h:189)
# SGIX_fbconfig (/usr/include/GL/glxext.h:195)
# SGIX_pbuffer (/usr/include/GL/glxext.h:209)
# SGI_cushion (/usr/include/GL/glxext.h:237)
# SGIX_video_resize (/usr/include/GL/glxext.h:240)
# SGIX_dmbuffer (/usr/include/GL/glxext.h:245)
# SGIX_swap_group (/usr/include/GL/glxext.h:249)
# SGIX_swap_barrier (/usr/include/GL/glxext.h:252)
# SGIS_blended_overlay (/usr/include/GL/glxext.h:255)
# SGIS_shared_multisample (/usr/include/GL/glxext.h:259)
# SUN_get_transparent_index (/usr/include/GL/glxext.h:264)
# 3DFX_multisample (/usr/include/GL/glxext.h:267)
# MESA_copy_sub_buffer (/usr/include/GL/glxext.h:272)
# MESA_pixmap_colormap (/usr/include/GL/glxext.h:275)
# MESA_release_buffers (/usr/include/GL/glxext.h:278)
# MESA_set_3dfx_mode (/usr/include/GL/glxext.h:281)
# SGIX_visual_select_group (/usr/include/GL/glxext.h:286)
# OML_swap_method (/usr/include/GL/glxext.h:290)
# OML_sync_control (/usr/include/GL/glxext.h:297)
# NV_float_buffer (/usr/include/GL/glxext.h:300)
# SGIX_hyperpipe (/usr/include/GL/glxext.h:304)
# MESA_agp_offset (/usr/include/GL/glxext.h:317)
# EXT_fbconfig_packed_float (/usr/include/GL/glxext.h:320)
# EXT_framebuffer_sRGB (/usr/include/GL/glxext.h:325)
# EXT_texture_from_pixmap (/usr/include/GL/glxext.h:329)
# NV_present_video (/usr/include/GL/glxext.h:365)
# NV_video_out (/usr/include/GL/glxext.h:369)
# NV_swap_group (/usr/include/GL/glxext.h:382)
# NV_video_capture (/usr/include/GL/glxext.h:385)
# EXT_swap_control (/usr/include/GL/glxext.h:391)
# NV_copy_image (/usr/include/GL/glxext.h:396)
# ARB_get_proc_address (/usr/include/GL/glxext.h:402)
# SGIX_video_source (/usr/include/GL/glxext.h:406)
# SGIX_fbconfig (/usr/include/GL/glxext.h:410)
# SGIX_pbuffer (/usr/include/GL/glxext.h:415)
# NV_video_output (/usr/include/GL/glxext.h:432)
# NV_video_capture (/usr/include/GL/glxext.h:436)
# VERSION_1_3 (/usr/include/GL/glxext.h:477)
# VERSION_1_4 (/usr/include/GL/glxext.h:519)
# ARB_get_proc_address (/usr/include/GL/glxext.h:527)
# ARB_multisample (/usr/include/GL/glxext.h:535)
# ARB_fbconfig_float (/usr/include/GL/glxext.h:539)
# ARB_create_context (/usr/include/GL/glxext.h:543)
# ARB_create_context_profile (/usr/include/GL/glxext.h:551)
# SGIS_multisample (/usr/include/GL/glxext.h:555)
# EXT_visual_info (/usr/include/GL/glxext.h:559)
# SGI_swap_control (/usr/include/GL/glxext.h:563)
# SGI_video_sync (/usr/include/GL/glxext.h:571)
# SGI_make_current_read (/usr/include/GL/glxext.h:581)
# SGIX_video_source (/usr/include/GL/glxext.h:591)
# EXT_visual_rating (/usr/include/GL/glxext.h:603)
# EXT_import_context (/usr/include/GL/glxext.h:607)
# SGIX_fbconfig (/usr/include/GL/glxext.h:623)
# SGIX_pbuffer (/usr/include/GL/glxext.h:641)
# SGI_cushion (/usr/include/GL/glxext.h:657)
# SGIX_video_resize (/usr/include/GL/glxext.h:665)
# SGIX_dmbuffer (/usr/include/GL/glxext.h:681)
# SGIX_swap_group (/usr/include/GL/glxext.h:691)
# SGIX_swap_barrier (/usr/include/GL/glxext.h:699)
# SUN_get_transparent_index (/usr/include/GL/glxext.h:709)
# MESA_copy_sub_buffer (/usr/include/GL/glxext.h:717)
# MESA_pixmap_colormap (/usr/include/GL/glxext.h:725)
# MESA_release_buffers (/usr/include/GL/glxext.h:733)
# MESA_set_3dfx_mode (/usr/include/GL/glxext.h:741)
# SGIX_visual_select_group (/usr/include/GL/glxext.h:749)
# OML_swap_method (/usr/include/GL/glxext.h:753)
# OML_sync_control (/usr/include/GL/glxext.h:757)
# NV_float_buffer (/usr/include/GL/glxext.h:773)
# SGIX_hyperpipe (/usr/include/GL/glxext.h:777)
# MESA_agp_offset (/usr/include/GL/glxext.h:824)
# EXT_fbconfig_packed_float (/usr/include/GL/glxext.h:832)
# EXT_framebuffer_sRGB (/usr/include/GL/glxext.h:836)
# EXT_texture_from_pixmap (/usr/include/GL/glxext.h:840)
# NV_present_video (/usr/include/GL/glxext.h:850)
# NV_video_output (/usr/include/GL/glxext.h:860)
# NV_swap_group (/usr/include/GL/glxext.h:878)
# NV_video_capture (/usr/include/GL/glxext.h:896)
# EXT_swap_control (/usr/include/GL/glxext.h:912)
# NV_copy_image (/usr/include/GL/glxext.h:920)
# NV_vertex_array_range (/usr/include/GL/glx.h:349)
GLsizei = c_int 	# /usr/include/GL/gl.h:163
GLfloat = c_float 	# /usr/include/GL/gl.h:164
# /usr/include/GL/glx.h:352
glXAllocateMemoryNV = _link_function('glXAllocateMemoryNV', POINTER(c_void), [GLsizei, GLfloat, GLfloat, GLfloat], 'NV_vertex_array_range')

GLvoid = None 	# /usr/include/GL/gl.h:156
# /usr/include/GL/glx.h:353
glXFreeMemoryNV = _link_function('glXFreeMemoryNV', None, [POINTER(GLvoid)], 'NV_vertex_array_range')

PFNGLXALLOCATEMEMORYNVPROC = CFUNCTYPE(POINTER(c_void), GLsizei, GLfloat, GLfloat, GLfloat) 	# /usr/include/GL/glx.h:354
PFNGLXFREEMEMORYNVPROC = CFUNCTYPE(None, POINTER(GLvoid)) 	# /usr/include/GL/glx.h:355
# MESA_allocate_memory (/usr/include/GL/glx.h:363)
GLX_MESA_allocate_memory = 1 	# /usr/include/GL/glx.h:364
# /usr/include/GL/glx.h:366
glXAllocateMemoryMESA = _link_function('glXAllocateMemoryMESA', POINTER(c_void), [POINTER(Display), c_int, c_size_t, c_float, c_float, c_float], 'MESA_allocate_memory')

# /usr/include/GL/glx.h:367
glXFreeMemoryMESA = _link_function('glXFreeMemoryMESA', None, [POINTER(Display), c_int, POINTER(None)], 'MESA_allocate_memory')

GLuint = c_uint 	# /usr/include/GL/gl.h:162
# /usr/include/GL/glx.h:368
glXGetMemoryOffsetMESA = _link_function('glXGetMemoryOffsetMESA', GLuint, [POINTER(Display), c_int, POINTER(None)], 'MESA_allocate_memory')

PFNGLXALLOCATEMEMORYMESAPROC = CFUNCTYPE(POINTER(c_void), POINTER(Display), c_int, c_size_t, c_float, c_float, c_float) 	# /usr/include/GL/glx.h:369
PFNGLXFREEMEMORYMESAPROC = CFUNCTYPE(None, POINTER(Display), c_int, POINTER(None)) 	# /usr/include/GL/glx.h:370
PFNGLXGETMEMORYOFFSETMESAPROC = CFUNCTYPE(GLuint, POINTER(Display), c_int, POINTER(None)) 	# /usr/include/GL/glx.h:371
# ARB_render_texture (/usr/include/GL/glx.h:380)
GLX_ARB_render_texture = 1 	# /usr/include/GL/glx.h:381
# /usr/include/GL/glx.h:383
glXBindTexImageARB = _link_function('glXBindTexImageARB', c_int, [POINTER(Display), GLXPbuffer, c_int], 'ARB_render_texture')

# /usr/include/GL/glx.h:384
glXReleaseTexImageARB = _link_function('glXReleaseTexImageARB', c_int, [POINTER(Display), GLXPbuffer, c_int], 'ARB_render_texture')

# /usr/include/GL/glx.h:385
glXDrawableAttribARB = _link_function('glXDrawableAttribARB', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int)], 'ARB_render_texture')

# NV_float_buffer (/usr/include/GL/glx.h:393)
# MESA_swap_frame_usage (/usr/include/GL/glx.h:405)
GLX_MESA_swap_frame_usage = 1 	# /usr/include/GL/glx.h:406
# /usr/include/GL/glx.h:408
glXGetFrameUsageMESA = _link_function('glXGetFrameUsageMESA', c_int, [POINTER(Display), GLXDrawable, POINTER(c_float)], 'MESA_swap_frame_usage')

# /usr/include/GL/glx.h:409
glXBeginFrameTrackingMESA = _link_function('glXBeginFrameTrackingMESA', c_int, [POINTER(Display), GLXDrawable], 'MESA_swap_frame_usage')

# /usr/include/GL/glx.h:410
glXEndFrameTrackingMESA = _link_function('glXEndFrameTrackingMESA', c_int, [POINTER(Display), GLXDrawable], 'MESA_swap_frame_usage')

# /usr/include/GL/glx.h:411
glXQueryFrameTrackingMESA = _link_function('glXQueryFrameTrackingMESA', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_float)], 'MESA_swap_frame_usage')

PFNGLXGETFRAMEUSAGEMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_float)) 	# /usr/include/GL/glx.h:413
PFNGLXBEGINFRAMETRACKINGMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable) 	# /usr/include/GL/glx.h:414
PFNGLXENDFRAMETRACKINGMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable) 	# /usr/include/GL/glx.h:415
PFNGLXQUERYFRAMETRACKINGMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_float)) 	# /usr/include/GL/glx.h:416
# MESA_swap_control (/usr/include/GL/glx.h:425)
GLX_MESA_swap_control = 1 	# /usr/include/GL/glx.h:426
# /usr/include/GL/glx.h:428
glXSwapIntervalMESA = _link_function('glXSwapIntervalMESA', c_int, [c_uint], 'MESA_swap_control')

# /usr/include/GL/glx.h:429
glXGetSwapIntervalMESA = _link_function('glXGetSwapIntervalMESA', c_int, [], 'MESA_swap_control')

PFNGLXSWAPINTERVALMESAPROC = CFUNCTYPE(c_int, c_uint) 	# /usr/include/GL/glx.h:431
PFNGLXGETSWAPINTERVALMESAPROC = CFUNCTYPE(c_int) 	# /usr/include/GL/glx.h:432
# EXT_texture_from_pixmap (/usr/include/GL/glx.h:442)
class struct_anon_111(Structure):
    __slots__ = [
        'event_type',
        'draw_type',
        'serial',
        'send_event',
        'display',
        'drawable',
        'buffer_mask',
        'aux_buffer',
        'x',
        'y',
        'width',
        'height',
        'count',
    ]
struct_anon_111._fields_ = [
    ('event_type', c_int),
    ('draw_type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('drawable', GLXDrawable),
    ('buffer_mask', c_uint),
    ('aux_buffer', c_uint),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('count', c_int),
]

GLXPbufferClobberEvent = struct_anon_111 	# /usr/include/GL/glx.h:508
class struct___GLXEvent(Union):
    __slots__ = [
        'glxpbufferclobber',
        'pad',
    ]
struct___GLXEvent._fields_ = [
    ('glxpbufferclobber', GLXPbufferClobberEvent),
    ('pad', c_long * 24),
]

GLXEvent = struct___GLXEvent 	# /usr/include/GL/glx.h:513

__all__ = ['GLX_VERSION_1_1', 'GLX_VERSION_1_2', 'GLX_VERSION_1_3',
'GLX_VERSION_1_4', 'GLX_USE_GL', 'GLX_BUFFER_SIZE', 'GLX_LEVEL', 'GLX_RGBA',
'GLX_DOUBLEBUFFER', 'GLX_STEREO', 'GLX_AUX_BUFFERS', 'GLX_RED_SIZE',
'GLX_GREEN_SIZE', 'GLX_BLUE_SIZE', 'GLX_ALPHA_SIZE', 'GLX_DEPTH_SIZE',
'GLX_STENCIL_SIZE', 'GLX_ACCUM_RED_SIZE', 'GLX_ACCUM_GREEN_SIZE',
'GLX_ACCUM_BLUE_SIZE', 'GLX_ACCUM_ALPHA_SIZE', 'GLX_BAD_SCREEN',
'GLX_BAD_ATTRIBUTE', 'GLX_NO_EXTENSION', 'GLX_BAD_VISUAL', 'GLX_BAD_CONTEXT',
'GLX_BAD_VALUE', 'GLX_BAD_ENUM', 'GLX_VENDOR', 'GLX_VERSION',
'GLX_EXTENSIONS', 'GLX_CONFIG_CAVEAT', 'GLX_DONT_CARE', 'GLX_X_VISUAL_TYPE',
'GLX_TRANSPARENT_TYPE', 'GLX_TRANSPARENT_INDEX_VALUE',
'GLX_TRANSPARENT_RED_VALUE', 'GLX_TRANSPARENT_GREEN_VALUE',
'GLX_TRANSPARENT_BLUE_VALUE', 'GLX_TRANSPARENT_ALPHA_VALUE', 'GLX_WINDOW_BIT',
'GLX_PIXMAP_BIT', 'GLX_PBUFFER_BIT', 'GLX_AUX_BUFFERS_BIT',
'GLX_FRONT_LEFT_BUFFER_BIT', 'GLX_FRONT_RIGHT_BUFFER_BIT',
'GLX_BACK_LEFT_BUFFER_BIT', 'GLX_BACK_RIGHT_BUFFER_BIT',
'GLX_DEPTH_BUFFER_BIT', 'GLX_STENCIL_BUFFER_BIT', 'GLX_ACCUM_BUFFER_BIT',
'GLX_NONE', 'GLX_SLOW_CONFIG', 'GLX_TRUE_COLOR', 'GLX_DIRECT_COLOR',
'GLX_PSEUDO_COLOR', 'GLX_STATIC_COLOR', 'GLX_GRAY_SCALE', 'GLX_STATIC_GRAY',
'GLX_TRANSPARENT_RGB', 'GLX_TRANSPARENT_INDEX', 'GLX_VISUAL_ID', 'GLX_SCREEN',
'GLX_NON_CONFORMANT_CONFIG', 'GLX_DRAWABLE_TYPE', 'GLX_RENDER_TYPE',
'GLX_X_RENDERABLE', 'GLX_FBCONFIG_ID', 'GLX_RGBA_TYPE',
'GLX_COLOR_INDEX_TYPE', 'GLX_MAX_PBUFFER_WIDTH', 'GLX_MAX_PBUFFER_HEIGHT',
'GLX_MAX_PBUFFER_PIXELS', 'GLX_PRESERVED_CONTENTS', 'GLX_LARGEST_PBUFFER',
'GLX_WIDTH', 'GLX_HEIGHT', 'GLX_EVENT_MASK', 'GLX_DAMAGED', 'GLX_SAVED',
'GLX_WINDOW', 'GLX_PBUFFER', 'GLX_PBUFFER_HEIGHT', 'GLX_PBUFFER_WIDTH',
'GLX_RGBA_BIT', 'GLX_COLOR_INDEX_BIT', 'GLX_PBUFFER_CLOBBER_MASK',
'GLX_SAMPLE_BUFFERS', 'GLX_SAMPLES', 'GLXContext', 'GLXPixmap', 'GLXDrawable',
'GLXFBConfig', 'GLXFBConfigID', 'GLXContextID', 'GLXWindow', 'GLXPbuffer',
'glXChooseVisual', 'glXCreateContext', 'glXDestroyContext', 'glXMakeCurrent',
'glXCopyContext', 'glXSwapBuffers', 'glXCreateGLXPixmap',
'glXDestroyGLXPixmap', 'glXQueryExtension', 'glXQueryVersion', 'glXIsDirect',
'glXGetConfig', 'glXGetCurrentContext', 'glXGetCurrentDrawable', 'glXWaitGL',
'glXWaitX', 'glXUseXFont', 'glXQueryExtensionsString', 'glXQueryServerString',
'glXGetClientString', 'glXGetCurrentDisplay', 'glXChooseFBConfig',
'glXGetFBConfigAttrib', 'glXGetFBConfigs', 'glXGetVisualFromFBConfig',
'glXCreateWindow', 'glXDestroyWindow', 'glXCreatePixmap', 'glXDestroyPixmap',
'glXCreatePbuffer', 'glXDestroyPbuffer', 'glXQueryDrawable',
'glXCreateNewContext', 'glXMakeContextCurrent', 'glXGetCurrentReadDrawable',
'glXQueryContext', 'glXSelectEvent', 'glXGetSelectedEvent',
'PFNGLXGETFBCONFIGSPROC', 'PFNGLXCHOOSEFBCONFIGPROC',
'PFNGLXGETFBCONFIGATTRIBPROC', 'PFNGLXGETVISUALFROMFBCONFIGPROC',
'PFNGLXCREATEWINDOWPROC', 'PFNGLXDESTROYWINDOWPROC', 'PFNGLXCREATEPIXMAPPROC',
'PFNGLXDESTROYPIXMAPPROC', 'PFNGLXCREATEPBUFFERPROC',
'PFNGLXDESTROYPBUFFERPROC', 'PFNGLXQUERYDRAWABLEPROC',
'PFNGLXCREATENEWCONTEXTPROC', 'PFNGLXMAKECONTEXTCURRENTPROC',
'PFNGLXGETCURRENTREADDRAWABLEPROC', 'PFNGLXGETCURRENTDISPLAYPROC',
'PFNGLXQUERYCONTEXTPROC', 'PFNGLXSELECTEVENTPROC',
'PFNGLXGETSELECTEDEVENTPROC', 'GLX_ARB_get_proc_address', '__GLXextFuncPtr',
'glXGetProcAddressARB', 'glXGetProcAddress', 'PFNGLXGETPROCADDRESSPROC',
'glXAllocateMemoryNV', 'glXFreeMemoryNV', 'PFNGLXALLOCATEMEMORYNVPROC',
'PFNGLXFREEMEMORYNVPROC', 'GLX_MESA_allocate_memory', 'glXAllocateMemoryMESA',
'glXFreeMemoryMESA', 'glXGetMemoryOffsetMESA', 'PFNGLXALLOCATEMEMORYMESAPROC',
'PFNGLXFREEMEMORYMESAPROC', 'PFNGLXGETMEMORYOFFSETMESAPROC',
'GLX_ARB_render_texture', 'glXBindTexImageARB', 'glXReleaseTexImageARB',
'glXDrawableAttribARB', 'GLX_MESA_swap_frame_usage', 'glXGetFrameUsageMESA',
'glXBeginFrameTrackingMESA', 'glXEndFrameTrackingMESA',
'glXQueryFrameTrackingMESA', 'PFNGLXGETFRAMEUSAGEMESAPROC',
'PFNGLXBEGINFRAMETRACKINGMESAPROC', 'PFNGLXENDFRAMETRACKINGMESAPROC',
'PFNGLXQUERYFRAMETRACKINGMESAPROC', 'GLX_MESA_swap_control',
'glXSwapIntervalMESA', 'glXGetSwapIntervalMESA', 'PFNGLXSWAPINTERVALMESAPROC',
'PFNGLXGETSWAPINTERVALMESAPROC', 'GLXPbufferClobberEvent', 'GLXEvent']
# END GENERATED CONTENT (do not edit above this line)

# From glxproto.h
GLXBadContext = 0
GLXBadContextState = 1
GLXBadDrawable = 2
GLXBadPixmap = 3
GLXBadContextTag = 4
GLXBadCurrentWindow = 5
GLXBadRenderRequest = 6
GLXBadLargeRequest = 7
GLXUnsupportedPrivateRequest = 8
GLXBadFBConfig = 9
GLXBadPbuffer = 10
GLXBadCurrentDrawable = 11
GLXBadWindow = 12

__all__ += ['GLXBadContext', 'GLXBadContextState', 'GLXBadDrawable',
'GLXBadPixmap', 'GLXBadContextTag', 'GLXBadCurrentWindow',
'GLXBadRenderRequest', 'GLXBadLargeRequest', 'GLXUnsupportedPrivateRequest',
'GLXBadFBConfig', 'GLXBadPbuffer', 'GLXBadCurrentDrawable', 'GLXBadWindow']





