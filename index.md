
## Home ##

This is a simple python-based backend framework to create light websites.

The creation of a website using this framework has the next features:

- Simplicity.

- Perdurability.

- Portability.

- Modularity.

The creation of new pages is easy due the creation of this pages is done using markdown language.

The pages created with Markdown are converted directly to Html using a script in Python called md2html.py (this script is simple and can be done in another languages like C, C++, or using Matlab/Octave), so the full content of the pages is stored in pure Html.

Due the full website is converted directly from Markdown to Html, this website no depend of another language and tools that can be unstables/unsupported after a long time. So, this make perdurable along time.

As I mentioned before, the full website is saved in Html, therefore this website can be changed easily to a different host server.

In addition to this, the folders are well organized and can be used easily.

Be careful: In order to use this you should use the same format of the markdown files presented in this website.

### Using ###

Navigate to repository with cd, example:

```
$ cd /home/dennis/Desktop/framework-light-website   #for linux
$ cd D:\users\dennis\Desktop\framework-light-website   #for windows
```

To CREATE html files and NOT UPDATE:

```
$ python md2html-ubuntu.py   #for linux
$ python md2html-windows.py   #for windows
```

To CREATE html files and UPDATE:

```
$ ./update-ubuntu.sh   #for linux
$ ./update-windows.bat   #for ubuntu
```

Also, you can run the update script clicking in the update.sh file.

### Preview ###

Preview of the website [[https://dennishnf.github.io/framework-light-website/index.html](https://dennishnf.github.io/framework-light-website/index.html)!] in Chrome browser is shown in the next image:

![image](/image.png){400}!
<p style="text-align:center;"><i>Preview of the website</i></p>

### License ###

GNU General Public License, version 3 (GPLv3).

You can visit my personal website: [http://dennishnf.bitbucket.io](http://dennishnf.bitbucket.io)!.

