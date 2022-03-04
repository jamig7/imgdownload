# imgdownload
A really bad Python script to download all images from a website. I was bored.

## Why you should use it (what works)
- You shoudln't
- Downloads NFTs
- Bypasses Cloudflare bot detection using [Anorov's cloudflare-scrape](https://github.com/Anorov/cloudflare-scrape "Anorov/cloudflare-scrape")

## Why you shouldn't use it
- Some websites don't work
- It sucks

## Dependencies
```python
pip install cfscrape
pip install bs4
```

## Usage
```python
python3 imgdownload.py [url] [path]
```
E.g `python3 imgdownload.py http://my-web.site/gallery/ website-pics`
