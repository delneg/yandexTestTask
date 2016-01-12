import unittest
from yandex_intern import check_email as b
from yandex_intern import check_email_regex as r
'''
1. e-mail состоит из имени и доменной части, эти части разделяются символом "@";
2. доменная часть не короче 3 символов и не длиннее 256, является набором непустых строк, состоящих из символов a-z 0-9_- и разделенных точкой;
3. каждый компонент доменной части не может начинаться или заканчиваться символом "-";
4. имя (до @) не длиннее 128 символов, состоит из символов a-z0-9"._-;
5. в имени не допускаются две точки подряд;
6. если в имени есть двойные кавычки ", то они должны быть парными;
7. в имени могут встречаться символы "!,:", но только между парными двойными кавычками.
'''
class  bTest(unittest.TestCase):
    def test_username_domain_at_sign(self):
        self.assertTrue(b('test@yandex.ru'))
        self.assertTrue(b('test@yandex.ru.com.net'))
        self.assertFalse(b('test@'))
        self.assertFalse(b('test@yandex.ru@fd'))
        self.assertFalse(b('test@yandex.ru@@@@'))
        self.assertFalse(b('test'))
        self.assertFalse(b('test@yandex.r@.ra'))
        self.assertFalse(b('@yandex.ru'))
    def test_domain_length_symbols_dots(self):
        self.assertFalse(b('test@'+'ya.ru'*256))
        self.assertTrue(b('test@y.r'))
        self.assertFalse(b('test@..ru'))
        self.assertFalse(b('test@yandex.'))
        self.assertFalse(b('test@yandeA.ru'))
        self.assertTrue(b('test@ya-dex.a_.a.a.a.a.ru'))
    def test_domain_not_end_begin_dash(self):
        self.assertFalse(b('test@-yandex.ru'))
        self.assertFalse(b('test@yandex-.ru'))
        self.assertFalse(b('test@yand.-ex.ru'))
        self.assertFalse(b('test@yandex-.ru'))
        self.assertFalse(b('test@yandex.ru-'))
        self.assertFalse(b('test@-yandex.-ru-'))
        self.assertTrue(b('test@yan-d-ex.ru'))
    def test_username_length_symbols(self):
        self.assertTrue(b('d'*128+'@yandex.ru'))
        self.assertFalse(b('d'*129+'@yandex.ru'))
        self.assertTrue(b('test._-n""eg@yandex.ru'))
    def test_username_two_dots(self):
        self.assertTrue(b('teste.g@yandex.ru'))
        self.assertFalse(b('teste..g@yandex.ru'))
    def test_username_paired_quotation_marks(self):
        self.assertTrue(b('teste""g@yandex.ru'))
        self.assertFalse(b('de""test"g@yandex.ru'))
        self.assertFalse(b('teste"g@yandex.ru'))
    def test_username_symbols_between_marks(self):
        self.assertTrue(b('test"eh!,eh:"test@hodor.ru'))
        self.assertFalse(b('de!,::"elng"@spok.ru'))
        self.assertFalse(b('de"testg!",:test@sheldon.ru'))
class  rTest(unittest.TestCase):
    def test_username_domain_at_sign(self):
        self.assertTrue(r('test@yandex.ru'))
        self.assertTrue(r('test@yandex.ru.com.net'))
        self.assertFalse(r('test@'))
        self.assertFalse(r('test@yandex.ru@fd'))
        self.assertFalse(r('test@yandex.ru@@@@'))
        self.assertFalse(r('test'))
        self.assertFalse(r('test@yandex.r@.ra'))
        self.assertFalse(r('@yandex.ru'))
    def test_domain_length_symbols_dots(self):
        self.assertFalse(r('test@'+'ya.ru'*256))
        self.assertTrue(r('test@y.r'))
        self.assertFalse(r('test@..ru'))
        self.assertFalse(r('test@yandex.'))
        self.assertFalse(r('test@yandeA.ru'))
        self.assertTrue(r('test@ya-dex.a_.a.a.a.a.ru'))
    def test_domain_not_end_begin_dash(self):
        self.assertFalse(r('test@-yandex.ru'))
        self.assertFalse(r('test@yandex-.ru'))
        self.assertFalse(r('test@yand.-ex.ru'))
        self.assertFalse(r('test@yandex-.ru'))
        self.assertFalse(r('test@yandex.ru-'))
        self.assertFalse(r('test@-yandex.-ru-'))
        self.assertTrue(r('test@yan-d-ex.ru'))
    def test_username_length_symbols(self):
        self.assertTrue(r('d'*128+'@yandex.ru'))
        self.assertFalse(r('d'*129+'@yandex.ru'))
        self.assertTrue(r('test._-n""eg@yandex.ru'))
    def test_username_two_dots(self):
        self.assertTrue(r('teste.g@yandex.ru'))
        self.assertFalse(r('teste..g@yandex.ru'))
    def test_username_paired_quotation_marks(self):
        self.assertTrue(r('teste""g@yandex.ru'))
        self.assertFalse(r('de""test"g@yandex.ru'))
        self.assertFalse(r('teste"g@yandex.ru'))
    def test_username_symbols_between_marks(self):
        self.assertTrue(r('test"eh!,eh:"test@hodor.ru'))
        self.assertFalse(r('de!,::"etest"@spok.ru'))
        self.assertFalse(r('de"testg!",:test@sheldon.ru'))
if __name__ == '__main__':
    unittest.main()
