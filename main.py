from pyscript import display, document


def general_weighted_average(e):
    document.getElementById('student_info').innerHTML = ' '
    document.getElementById('summary').innerHTML = ' '
    document.getElementById('output').innerHTML = ' '
    subjects = ['Biology', 'Math', 'English', 'Japanese', 'ICT', 'Training']
    units_subject = (5, 3, 2, 1, 1)

    first_name = document.getElementById('last_name').value
    last_name = document.getElementById('first_name').value

    biology = float(document.getElementById('biology').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    japanese = float(document.getElementById('japanese').value)
    ict = float(document.getElementById('ict').value)
    training = float(document.getElementById('training').value)

    weighted_sum = (biology * units_subject[0] + 
           math * units_subject[1] + 
           english * units_subject[2] + 
           japanese * units_subject[3] + 
           ict * units_subject[4] + 
           training * units_subject[5]) 
    total_units = sum(units_subject)
    gwa = weighted_sum / total_units
    
    summary = f"""{subjects[0]}: {biology:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {japanese:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {training:.0f}
    """
    display(f'Name: {last_name} {first_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output', )