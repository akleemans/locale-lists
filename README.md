# locale-lists

A collection of locale lists.

* Android 5.1: [csv](locales/android.csv) | [json](locales/android.json) (645 locales, [source](https://stackoverflow.com/questions/7973023/what-is-the-list-of-supported-languages-locales-on-android))
* DuckDuckGo: [csv](locales/duckduckgo.csv) | [json](locales/duckduckgo.json) with translated names (100 locales, [source](https://github.com/duckduckgo/duckduckgo-locales) - April 2020)
* Facebook: [csv]() | [json]() (103 locales, [source](https://developers.facebook.com/docs/messenger-platform/messenger-profile/supported-locales/))
* iOS 9.3: [csv](locales/ios.csv), [json](locales/ios.json) (732 locales, [source](https://gist.github.com/jasef/337431c43c3addb2cbd5eb215b376179))
* Microsoft OpenSpec: [csv](locales/microsoft.csv) | [json](locales/microsoft.json) (829 locales, [source](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c))
* Umpirsky: [csv](locales/umpirsky.csv) | [json](locales/umpirsky.json) (563 locales, [source](https://github.com/umpirsky/locale-list/blob/master/data/en/locales.csv))
* Java 8: [csv](locales/java.csv) | [json](locales/java.json) (110 locales, [source](https://www.oracle.com/java/technologies/javase/jdk8-jre8-suported-locales.html))


## Notes

While browsing the internet & searching for a locale list I found a lot of different lists in different formats, so this is a collection of some of them in a consistent format.

These [locales](https://en.wikipedia.org/wiki/Locale_(computer_software) usually follow the [BCP 47](https://tools.ietf.org/rfc/bcp/bcp47.txt) format with a two-letter, lowercase language code (like `en` or `de`) and a two-letter uppercase country code (like `US` or `CH`).
As most of the sources use a underscore (`_`) instead of a hyphen (`-`) I adopted that so the locales look like `en_US` or `de_CH`.

Besides this, there are other formats which some of the (mostly bigger) lists use:

* `en` - only language, no country
* `az_Latn_AZ` - additional Latin or Cyrillic (`Cyrl`) identifier
* `ar_001` - "Arabic (World)" / `en_001` - "English (World)" (or `en_150` - "English (Europe)")
* `eo_XX` - "Esperanto", `tokipona_XX` - "Toki Pona",

The selection is somewhat random and does not distinguish between "real" lists (with purpose of collecting locale tags) and usages (localized applications/websites).

If available, the locales have an english name. If not, this is mentioned in the list.

The CSV separator is `,` and the quote char (where needed) is `"`.
JSON format is a simple object with language tags as keys and names as values.
