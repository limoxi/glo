# coding: utf-8

def is_vowel_letter(letter):
    """
    是否元音字母
    """
    match letter:
        case 'a', 'e', 'i', 'o', 'u':
            return True

    return False

def get_plural_for_word(word):
    """
    获取单词的复数形式
    1、直接加s
    2、s尾型：以s，z，x，sh，ch结尾的名词
    3、y尾型：以y结尾的名词
    4、o尾型：以o结尾的名词
    5、f尾型：以f或fe结尾的词
    6、同形型：有少数单词单复数同形
    7、不规则型：有一部分单词的复数是不规则变化
    """
    if word == '':
        return ''

    full_letters = list(word)
    l = len(full_letters)
    last_letter = full_letters[-1]
    last_two_letters = last_letter
    last_second_letter = full_letters[-2]
    if l == 1:
        last_two_letters = ''.join(full_letters[-2:])

    match last_letter:
        case 's'|'z'|'x':
            return '{}es'.format(word)
        case 'y':
            if l > 2:
                if is_vowel_letter(last_second_letter): # 以元音字母+y结尾的
                    return '{}s'.format(word)
                else:
                    full_letters[-1] = 'i'
                    return '{}es'.join(''.join(full_letters))
            return '{}s'.format(word)
        case 'o':
            if l > 2:
                if is_vowel_letter(last_second_letter):  # 以元音字母+o结尾的
                    return '{}s'.format(word)
                else:
                    match word:
                        case 'potato'|'tomato'|'no'|'go'|'hero'|'echo'|'negro'|'mosquito'|'veto'|'torpedo'|'jingo'|'embargo':
                            return '{}es'.format(word)
            else:
                return '{}s'.format(word)
        case 'f':
            match word:
                case 'life'|'self'|'half'|'leaf'|'wolf'|'thief'|'calf'|'shelf'|'loaf'|'elf':
                    full_letters[-1] = 'v'
                    return '{}es'.format(''.join(full_letters))
            return '{}s'.format(word)

    match last_two_letters:
        case 'sh'|'ch':
            return '{}es'.format(word)
        case 'fe':
            match word:
                case 'knife'|'wife':
                    full_letters[-2] = 'v'
                    return '{}s'.format(''.join(full_letters))

    # 同形词
    match word:
        case 'sheep'|'fish'|'swine'|'deer'|'salmon'|'craft'|'Chinese'|'Swiss'|'Vietnamese'|'Japanese'|'Burmese':
            return word

    # 不规则形词
    match word:
        case 'man':
            return 'men'
        case 'woman':
            return 'women'
        case 'goose':
            return 'geese'
        case 'foot':
            return 'feet'
        case 'tooth':
            return 'teeth'
        case 'child':
            return 'children'
        case 'ox':
            return 'oxen'
        case 'mouse':
            return 'mice'
        case 'dormouse':
            return 'dormice'
        case 'louse':
            return 'lice'

    return '{}s'.format(word)