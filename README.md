# a minimal cowsay blog

usage:
    
    # Use your favorite editor to make deploy scp to the right place
    vi deploy
    
    # Make necessary directory for index
    mkdir cowposts_html
    
    # Moo!
    echo "hello world" > hello_world
    python cowpost.py hello_world
    . deploy
