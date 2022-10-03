# Password-Generator-Python
## Dependencies
```
python
git
<Your Favorite Terminal>
```
## Installation
Use `git clone` to clone this repository into your chosen directory. Navigate to your directory of choice and run `python .\main.py` for Windows users, or `python ./main.py` for users on Unix based machines.

Note: I recommend using the latest version of Python. This project was created using Python 3.10.6. Check out [pyenv](https://github.com/pyenv/pyenv) if you are struggling with a newer/older version of Python (and consider a pull request or opening an issue).

## Using the More Secure Option
In this tool, you may choose to use the reasonably secure option that instead taking from the [secret](https://docs.python.org/3/library/secrets.html) module rather than the [random](https://docs.python.org/3/library/random.html#module-random) module. Do keep in mind that I do not have the time and resources to personally audit this project and would simply redirect any users of this project to [KeePassXC](https://github.com/keepassxreboot/keepassxc) for a more ideal option.

When in doubt, please do use the more secure option. Entering 'N' for your input is going to generate a password using a pseudo-random generator. Click [here](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) for a basic overview of security implications at play and decide for yourself what is most appropriate. While the link is more specifically about pseudo-random *number* generators, the general concept should be enough for your consideration.
