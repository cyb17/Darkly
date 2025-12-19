# Hidden directory exposed via robots.txt

## How do we find the breach ?

We visited the `robots.txt`file, there was a `.hidden` directory with a lot of others directories inside, and each of them had a `README` file. So we created a script to crawl each README files, and the flag was hidden in one of them.

```
[+] http://192.168.56.102/.hidden//whtccjokayshttvxycsvykxcfm//igeemtxnvexvxezqwntmzjltkt//kbjjgbfcbchslgysntmtmcxzyr//README
Non ce n'est toujours pas bon ...
[+] http://192.168.56.102/.hidden//whtccjokayshttvxycsvykxcfm//igeemtxnvexvxezqwntmzjltkt//lmpanswobhwcozdqixbowvbrhw//README
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
[+] http://192.168.56.102/.hidden//whtccjokayshttvxycsvykxcfm//igeemtxnvexvxezqwntmzjltkt//mfmtemmsbpftlvuuuwitbydbbt//README
Toujours pas tu vas craquer non ?
[+] http://192.168.56.102/.hidden//whtccjokayshttvxycsvykxcfm//igeemtxnvexvxezqwntmzjltkt//nzzuqitxumdibwksdfdbczvahq//README
Tu veux de l'aide ? Moi aussi !  
[+] http://192.168.56.102/.hidden//whtccjokayshttvxycsvykxcfm//igeemtxnvexvxezqwntmzjltkt//oehtfkmejiwsbvoqyztwllaqqb//README
```

**robots.txt** : robots.txt is the filename used for implementing the Robots Exclusion Protocol, a standard used by websites to indicate to visiting web crawlers and other web robots which portions of the website they are allowed to visit.  
Not every website has a robots.txt file; it is optional and only serves to give crawling instructions to search engine bots.

## How to exploit the breach ?

A misconfigured or unprotected robots.txt can reveal sensitive directories, give attackers clues about site structure, and cause unintended indexing of private pages. It is not a security mechanism.

## How to avoid the breach ?

The robots.txt file should never list sensitive directories. All sensitive resources must be protected by proper access controls and HTTPS. robots.txt should only be used for SEO purposes.