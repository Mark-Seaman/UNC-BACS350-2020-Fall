from markdown import markdown


def lorem(num_chars):
    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium quibusdam sit hic, ipsum labore commodi eligendi quos culpa maxime voluptate. Ad, voluptatem, esse! Quam accusantium minus sequi cumque minima quod odio accusamus assumenda dolorem consequuntur esse alias nisi, explicabo error! Dolores blanditiis adipisci laboriosam quo sequi nostrum consectetur recusandae illo sed molestias laborum, ullam modi doloremque. Facilis nulla iure odit accusamus. Doloremque voluptatibus repudiandae, beatae temporibus odit suscipit eius facere dolores quibusdam perspiciatis exercitationem velit porro cupiditate repellendus et tempora dolorem, sapiente, debitis cum nihil sunt. Illo perspiciatis cumque qui quia quam quibusdam doloribus fugiat porro, soluta esse nesciunt itaque? Blanditiis, voluptate, voluptates iure iste aut maxime perferendis aliquid, odit doloribus sapiente temporibus ad mollitia consequuntur, alias totam tenetur ut. Accusantium voluptas temporibus, ea a impedit.'''
    return text[:num_chars]
    
    
def card_data():
    return dict(title="Card Layout", body=lorem(200), color="bg-success")


def cards_data():
    return [
                dict(title="Card One", body=lorem(200), color="bg-success"),
                dict(title="Card Two", body=lorem(150), color="bg-primary"),
                dict(title="Card Three", body=lorem(350), color="bg-warning"),
                dict(title="Card Four", body=lorem(500), color="bg-danger"),
            ]


def markdown_data(doc):
    return dict(title=doc, html=markdown(open(doc).read()))



#def accordion_data():
#
#    def card_content(i, active):
#        card = dict(id=i, title=f'Week {i+1}', body=text)
#        if i == active:
#            card['show'] = 'show'
#            card['active'] = 'true'
#        return card
#
#    return [card_content(i, 0) for i in range(7)]
#
#
#def tabs_data():
#
#    def options(i, tab, selected):
#        if selected:
#            return dict(name=f'tab{i}', header=tab[0], body=tab[1],
#                        active='active', show='show', selected='true')
#        else:
#            return dict(name=f'tab{i}', header=tab[0], body=tab[1],
#                        active='', show='', selected='false')
#
#    tabs = ('Tab 1', text), ('Tab 2', text)
#    return [options(i, tab, i == 0) for i, tab in enumerate(tabs)]
#

