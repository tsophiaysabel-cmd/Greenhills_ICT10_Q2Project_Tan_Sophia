from pyscript import display

person = {
    'name': 'Sophia Tan',
    'tagline': 'Student, aspiring artist, and science enthusiast.',
    'about': "I'm a person who loves making art. I also enjoy a lot of shows, anime, and comics.",
    'quote': 'Dum Spiro Spero',
    'quote_by': 'Latin Proverb'
}

interests = ['Drawing', 'Chiikawa', 'Makeup']
hobbies = ['Making art', 'Watching shows', 'Cooking']
dreams = ['Ace the science QE and get a flask from Mr. Calpo.']

quote = person.get('quote')
quote_by = person.get('quote_by')

display('Meet Me', target='output')
display(person.get('name'), target='output')
display(person.get('tagline'), target='output')

display('About me', target='output')
display(person.get('about'), target='output')

display('Interests', target='output')
display(', '.join(interests), target='output')

display('Hobbies', target='output')
display(', '.join(hobbies), target='output')

display('Dreams', target='output')
display(', '.join(dreams), target='output')

display(f'"{quote}" - {quote_by}', target='output')