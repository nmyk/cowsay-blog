# a minimal cowsay blog

usage:
    
    # Use your favorite editor to make deploy scp to the right place
    vi deploy
    
    # Make necessary directories
    mkdir posts cowposts cowposts_html
    
    # Moo!
    echo "hello world" > hello_world
    . cowpost hello_world
    . deploy
