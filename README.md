# Sample application to learn docker based deployment of DL models. 

This implementation is docker based deployment of done on fashio_mnist dataset. This is very basic code to new entrants to undersand docker based deployments. 

The main code is app.py qhich you need to run to test the code.

There is also an html web API implementation that can be accessed via de-commenting the code and commenting others (return value).

For Docker based deployments, run in following serquence
1. Clone the repo : git clone https://github.com/tejas2454/testing.git
2. setup vitrual env(recommended)
    pip install virtualenv
    cd my-project/
    virtualenv venv
    virtualenv venv --system-site-packages
    source venv/bin/activate

    #To start Virtual Environment:
    source venv/bin/activate
    source ~/.bash_profile
3. sudo docker build -t test_deployment .
4. sudo docker run -p127.0.0.1:9082:9082 test_deployment 

and you will be getting the IP to evaluate results. Setup configurations into nginx as per requirement to access globally. 
