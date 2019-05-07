# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/Capsicum
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1 (prototype)


from aqt import mw
from anki.template import Template
from anki.hooks import wrap
import re, os

# from anki import version
# ANKI20=version.startswith("2.0.")


re_cloze = re.compile(r"(?s)\{\{c\d+::(.*?)(::(.*?))?\}\}")


def repl(m):
    return '<span class="C1023">%s</span>'%(m.group(0))
    #Use css/html to differentiate front/back side
    #and apply color only to the back side.


def render_sections(self, template, context, _old):
    for field in context:
        txt=context[field]
        if re_cloze.search(txt):
            context[field]=re.sub(re_cloze,repl,txt)
    return _old(self, template, context)

Template.render_sections = wrap(Template.render_sections, render_sections, 'around')

