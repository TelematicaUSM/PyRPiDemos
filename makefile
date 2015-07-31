PHONY = clean runenv

env = env
runenv = . $(env)/bin/activate
python = $(runenv) && python
pip_install = $(runenv) && pip install

$(env): requirements.txt
	virtualenv --python=python3 $(env)
	$(pip_install) -r requirements.txt

%: %.py | env
	sudo sh -c "$(python) $<"

clean:
	rm -rf $(env) __pycache__ *.pyc
