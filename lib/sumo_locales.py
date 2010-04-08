# -*- coding: utf-8 -*-
from collections import namedtuple

Language = namedtuple(u'Language', u'external internal english native dictionary')

languages = {
    u'af': Language(u'af', u'af', u'Afrikaans', u'Afrikaans', u'af-NA'),
    u'ak': Language(u'ak', u'ak', u'Akan', u'Akan', u'ak-GH'),
    u'ast-ES': Language(u'ast-ES', u'ast-ES', u'Asturian', u'Asturianu', u'ast-ES'),
    u'ar': Language(u'ar', u'ar', u'Arabic', u'عربي', u'ar'),
    u'as': Language(u'as', u'as', u'Assamese', u'অসমীয়া', u'as-'),
    u'be': Language(u'be', u'be', u'Belarusian', u'Беларуская', u'be'),
    u'bg': Language(u'bg', u'bg', u'Bulgarian', u'Български', u'bg'),
    u'bn-BD': Language(u'bn-BD', u'bn-BD', u'Bengali (Bangladesh)', u'বাংলা (বাংলাদেশ)', u'bn-BD'),
    u'bn-IN': Language(u'bn-IN', u'bn-IN', u'Bengali (India)', u'বাংলা (ভারত)', u'bn-IN'),
    u'br-FR': Language(u'br-FR', u'br-FR', u'Breton', u'Brezhoneg', u'br-FR'),
    u'ca': Language(u'ca', u'ca', u'Catalan', u'català', u'ca'),
    u'cs': Language(u'cs', u'cs', u'Czech', u'Čeština', u'cs'),
    u'cy': Language(u'cy', u'cy', u'Welsh', u'Cymraeg', u'cy'),
    u'da': Language(u'da', u'da', u'Danish', u'Dansk', u'da'),
    u'de': Language(u'de', u'de', u'German', u'Deutsch', u'de-DE'),
    u'dsb': Language(u'dsb', u'dsb', u'Lower Sorbian', u'Dolnoserbšćina', u'dsb'),
    u'el': Language(u'el', u'el', u'Greek', u'Ελληνικά', u'el'),
    u'en-US': Language(u'en-US', u'en', u'English', u'English', u'en-US'),
    u'eo': Language(u'eo', u'eo', u'Esperanto', u'Esperanto', u'eo'),
    u'es': Language(u'es', u'es', u'Spanish', u'Español', u'es-ES'),
    u'et': Language(u'et', u'et', u'Estonian', u'Eesti keel', u'et'),
    u'eu': Language(u'eu', u'eu', u'Basque', u'Euskara', u'eu'),
    u'fa': Language(u'fa', u'fa', u'Persian', u'فارسی', u'fa'),
    u'fi': Language(u'fi', u'fi', u'Finnish', u'suomi', u'fi'),
    u'fj-FJ': Language(u'fj-FJ', u'fj-FJ', u'Fijian', u'Vosa vaka-Viti', u'fj-FJ'),
    u'fr': Language(u'fr', u'fr', u'French', u'Français', u'fr-FR'),
    u'fur': Language(u'fur', u'fur', u'Friulian', u'Furlan', u'fur-IT'),
    u'fy-NL': Language(u'fy-NL', u'fy-NL', u'Frisian', u'Frysk', u'fy-NL'),
    u'ga-IE': Language(u'ga-IE', u'ga-IE', u'Irish (Ireland)', u'Gaeilge (Éire)', u'ga-IE'),
    u'gl': Language(u'gl', u'gl', u'Galician', u'Galego', u'gl'),
    u'gu-IN': Language(u'gu-IN', u'gu-IN', u'Gujarati', u'ગુજરાતી', u'gu-IN'),
    u'he': Language(u'he', u'he', u'Hebrew', u'עברית', u'he'),
    u'hi': Language(u'hi', u'hi', u'Hindi', u'हिन्दी', u'hi'),
    u'hi-IN': Language(u'hi-IN', u'hi-IN', u'Hindi (India)', u'हिन्दी (भारत)', u'hi-IN'),
    u'hr': Language(u'hr', u'hr', u'Croatian', u'Hrvatski', u'hr'),
    u'hsb': Language(u'hsb', u'hsb', u'Upper Sorbian', u'Hornjoserbsce', u'hsb'),
    u'hu': Language(u'hu', u'hu', u'Hungarian', u'Magyar', u'hu'),
    u'hy-AM': Language(u'hy-AM', u'hy-AM', u'Armenian', u'Հայերեն', u'hy-AM'),
    u'id': Language(u'id', u'id', u'Indonesian', u'Bahasa Indonesia', u'id'),
    u'is': Language(u'is', u'is', u'Icelandic', u'íslenska', u'is'),
    u'it': Language(u'it', u'it', u'Italian', u'Italiano', u'it'),
    u'ja': Language(u'ja', u'ja', u'Japanese', u'日本語', u'ja'),
    u'ka': Language(u'ka', u'ka', u'Georgian', u'ქართული', u'ka'),
    u'kk': Language(u'kk', u'kk', u'Kazakh', u'Қазақ', u'kk'),
    u'kn': Language(u'kn', u'kn', u'Kannada', u'ಕನ್ನಡ', u'kn'),
    u'ko': Language(u'ko', u'ko', u'Korean', u'한국어', u'ko'),
    u'ku': Language(u'ku', u'ku', u'Kurdish', u'Kurdî', u'ku'),
    u'lt': Language(u'lt', u'lt', u'Lithuanian', u'lietuvių kalba', u'lt'),
    u'lv': Language(u'lv', u'lv', u'Latvian', u'Latviešu', u'lv'),
    u'mg': Language(u'mg', u'mg', u'Malagasy', u'Malagasy', u'mg'),
    u'mi': Language(u'mi', u'mi', u'Maori (Aotearoa)', u'Māori (Aotearoa)', u'mi'),
    u'mk': Language(u'mk', u'mk', u'Macedonian', u'Македонски', u'mk'),
    u'ml': Language(u'ml', u'ml', u'Malayalam', u'മലയാളം', u'ml'),
    u'mn': Language(u'mn', u'mn', u'Mongolian', u'Монгол', u'mn'),
    u'mr': Language(u'mr', u'mr', u'Marathi', u'मराठी', u'mr'),
    u'ms': Language(u'ms', u'ms', u'Malay', u'بهاس ملايو', u'ms'),
    u'nb-NO': Language(u'nb-NO', u'nb-NO', u'Norwegian (Bokmål)', u'Norsk bokmål', u'nb-NO'),
    u'ne-NP': Language(u'ne-NP', u'ne-NP', u'Nepali', u'नेपाली', u'ne-NP'),
    u'no': Language(u'no', u'no', u'Norwegian', u'Norsk nynorsk', u'nn-NO'),
    u'nl': Language(u'nl', u'nl', u'Dutch', u'Nederlands', u'nl'),
    u'nr': Language(u'nr', u'nr', u'Ndebele, South', u'isiNdebele', u'nr'),
    u'nso': Language(u'nso', u'nso', u'Northern Sotho', u'Sepedi', u'nso'),
    u'oc': Language(u'oc', u'oc', u'Occitan (Lengadocian)', u'occitan (lengadocian)', u'oc'),
    u'or': Language(u'or', u'or', u'Oriya', u'ଓଡ଼ିଆ', u'or'),
    u'pa-IN': Language(u'pa-IN', u'pa-IN', u'Punjabi', u'ਪੰਜਾਬੀ', u'pa-IN'),
    u'pl': Language(u'pl', u'pl', u'Polish', u'Polski', u'pl'),
    u'pt-BR': Language(u'pt-BR', u'pt-BR', u'Portuguese (Brazilian)', u'Português (do Brasil)', u'pt-BR'),
    u'pt-PT': Language(u'pt-PT', u'pt-PT', u'Portuguese (Portugal)', u'Português (Europeu)', u'pt-PT'),
    u'rm': Language(u'rm', u'rm', u'Romansh', u'rumantsch', u'rm'),
    u'ro': Language(u'ro', u'ro', u'Romanian', u'română', u'ro'),
    u'ru': Language(u'ru', u'ru', u'Russian', u'Русский', u'ru'),
    u'rw': Language(u'rw', u'rw', u'Kinyarwanda', u'Ikinyarwanda', u'rw'),
    u'si': Language(u'si', u'si', u'Sinhala', u'සිංහල', u'si'),
    u'sk': Language(u'sk', u'sk', u'Slovak', u'slovenčina', u'sk'),
    u'sl': Language(u'sl', u'sl', u'Slovenian', u'slovensko', u'sl'),
    u'sq': Language(u'sq', u'sq', u'Albanian', u'Shqip', u'sq'),
    u'sr-CYRL': Language(u'sr-CYRL', u'sr-CYRL', u'Serbian', u'Српски', u'sr-Cyrl'),
    u'sr-LATN': Language(u'sr-LATN', u'sr-LATN', u'Serbian', u'Srpski', u'sr-Latn'),
    u'ss': Language(u'ss', u'ss', u'Siswati', u'siSwati', u'ss'),
    u'st': Language(u'st', u'st', u'Southern Sotho', u'Sesotho', u'st'),
    u'sv-SE': Language(u'sv-SE', u'sv-SE', u'Swedish', u'Svenska', u'sv-SE'),
    u'ta': Language(u'ta', u'ta', u'Tamil', u'தமிழ்', u'ta'),
    u'ta-IN': Language(u'ta-IN', u'ta-IN', u'Tamil (India)', u'தமிழ் (இந்தியா)', u'ta-IN'),
    u'ta-LK': Language(u'ta-LK', u'ta-LK', u'Tamil (Sri Lanka)', u'தமிழ் (இலங்கை)', u'ta-LK'),
    u'te': Language(u'te', u'te', u'Telugu', u'తెలుగు', u'te'),
    u'th': Language(u'th', u'th', u'Thai', u'ไทย', u'th'),
    u'tn': Language(u'tn', u'tn', u'Tswana', u'Setswana', u'tn'),
    u'tr': Language(u'tr', u'tr', u'Turkish', u'Türkçe', u'tr'),
    u'ts': Language(u'ts', u'ts', u'Tsonga', u'Xitsonga', u'ts'),
    u'tt-RU': Language(u'tt-RU', u'tt-RU', u'Tatar', u'Tatarça', u'tt-RU'),
    u'uk': Language(u'uk', u'uk', u'Ukrainian', u'Українська', u'uk'),
    u'ur': Language(u'ur', u'ur', u'Urdu', u'اُردو', u'ur'),
    u've': Language(u've', u've', u'Venda', u'Tshivenḓa', u've'),
    u'vi': Language(u'vi', u'vi', u'Vietnamese', u'Tiếng Việt', u'vi'),
    u'wo': Language(u'wo', u'wo', u'Wolof', u'Wolof', u'wo'),
    u'xh': Language(u'xh', u'xh', u'Xhosa', u'isiXhosa', u'xh'),
    u'zh-CN': Language(u'zh-CN', u'zh-CN', u'Chinese (Simplified)', u'中文 (简体)', u'zh-CN'),
    u'zh-TW': Language(u'zh-TW', u'zh-TW', u'Chinese (Traditional)', u'正體中文 (繁體)', u'zh-TW'),
    u'zu': Language(u'zu', u'zu', u'Zulu', u'isiZulu', u'zu'),
}