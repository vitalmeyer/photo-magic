from pyhtml import *


def get_pyhtml_dummypage():
    t = html(
        head(
            title('Awesome website'),
        ),
        body(
            header(

            ),
            div(
                'Content here'
            ),
            footer(
                hr,
                'Copyright 2013'
            )
        )
    )
    return t.render()

pics = """
{
    {Filename : <filename>
        {Lag: "33.2"}
        {Lng: "44.4"}
        {XXX: "foobar" }
    }
}
"""