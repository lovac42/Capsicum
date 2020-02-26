# Capsicum: Colorize Cloze Siblings


Note: This addon no longer works with the changes made to the templates in 2.1.20.


## About:
When using incremental cloze, I always forget whether I added the sibling text. This will colorize all the siblings so there's no need to check with the editor. This addon will add css tags to cloze siblings so you can stylize siblings with different colors. You can also use addon: "front or back" to isolate the front side and the back side.

<img src="https://github.com/lovac42/Capsicum/blob/master/screenshots/sib_cloze.png?raw=true">  


### Example:
```
.C1023 {
  color: aqua;
}
```

CSS may have changed and may not work.
```

.C1023 .card1 {
  color: navy;
}
.C1023 .card2 {
  color: pink;
}
.C1023 .card3 {
  color: lime;
}
```


## Compatibility:
This will not be compatible with the addon: nested cloze, which will have this feature built in.

