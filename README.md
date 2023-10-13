# integrate your fediverse timeline into your static blog! (without javascript!)


## Motivation
I'd like to include my posts on fediverse into my blog **without javascript**.
So I wrote a simple python script to fetch my posts via (Mastodon) server APIs
and parse the posts into a json file. My static site generator (hugo) then use
this data and render the posts into static HTML.

**Demo**(my own blog): https://shrik3.com/timeline/

## How to use

**Prerequisites**  
- [Mastodon.py](https://github.com/halcy/Mastodon.py/tree/3d5b94f07fab53d64e03fadb68b92eec496cbe13)
- python3.0 +
- Register a new bot account and follow your main account

**Usage**  
For the first time only, take a look at `config.py` and modify it. Most importantly
- `APPNAME` name it whatever you like
- `BASEURL` url of your instance
- `FOLLOW` your main account
- comment out the foolproof lines at the top of `config.py`.

```bash
./timelinebot.py`
````
You will be prompted to input credentials for the **bot** account (not your main
account!). After a successful login, the access token will be stored in
`token.secret` and you no longer need to log in manually.

The script will fetch your posts and store them in `tl.json`. Then you can preceed to
render this data into static pages with your site generator.

**For Hugo**  
create a partial in your template. Maybe take a look at `examples/hugo_timeline_partial.html`.

Everytime before you render the pages, run the timeline bot script and copy
`tl.json` into your blog's `data/` directory. For automation you may use
`examples/syncblog.sh`

**For non-pleroma users**  
Change the `feature_set` field in the code accordingly
```python
self.session = Mastodon(client_id=self.config.CLIENTID, access_token=self.config.TOKEN, feature_set="pleroma")
```

**Do not download other people's data without their permission!**
