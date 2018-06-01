from django import template
import re
register = template.Library()


@register.tag
def ifmatches(parser, token):
    lst = token.split_contents()
    val = lst[1]
    regex = lst[2]
    nodelist_true = parser.parse(('else','endifmatches',))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse(('endifmatches',))
        parser.delete_first_token()
    else:
        nodelist_false = template.NodeList()
    return MatchesRegexNode(nodelist_true, nodelist_false, val, regex)


class MatchesRegexNode(template.Node):
    def __init__(self, nodelist_true, nodelist_false, val, regex):
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false
        self.val = template.Variable(val)
        self.regex = regex.strip('"')

    def render(self, context):
        val = self.val.resolve(context)
        if re.search(self.regex, val):
            return self.nodelist_true.render(context)
        else:
            return self.nodelist_false.render(context)
