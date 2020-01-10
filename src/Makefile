# this is a Makefile for all the languages under dict

# to add a language:
# 1. add the language code to the LANGUAGES list
# 2. add a build rule for the language directory (see below for examples)
# 3. create the language directory and place the required files in there

LANGUAGES=af en_ZA tn sw xh zu

TARGETS=utils $(LANGUAGES)

.PHONY: all clean aspell myspell $(TARGETS)

all: $(TARGETS)

$(LANGUAGES): utils

export PATH:=$(PATH):$(shell (cd utils ; pwd))

af:
	$(MAKE) -C $@

en_ZA:
	$(MAKE) -C $@

sw: 
	$(MAKE) -C $@

tn: 
	$(MAKE) -C $@

xh: 
	$(MAKE) -C $@

zu:
	$(MAKE) -C $@

utils: 
	$(MAKE) -C $@

clean:
	$(foreach SUBDIR,$(TARGETS), $(MAKE) -C $(SUBDIR) clean ; )

aspell:
	$(foreach SUBDIR,$(LANGUAGES), $(MAKE) -C $(SUBDIR) aspell ; )

myspell:
	$(foreach SUBDIR,$(LANGUAGES), $(MAKE) -C $(SUBDIR) myspell ; )

wordlist:
	$(foreach SUBDIR,$(LANGUAGES), $(MAKE) -C $(SUBDIR) wordlist ; )
