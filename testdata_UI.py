
#-------------------------this is test data for contact form tests - UI---------------
#-------------correct - name, email, phone, subject, message
#regular correct set of data
testdata_correct_1 = [("John-Doe ŚĆ!@# 123"), ("mail-ŚĆ@mail.com"), ("+99 (645) 645-699"), ("Can I have discount? 123_)_)(*())ŚĆ"), 
                        ("hi, test message, I would like to know if I can get a discount for my next booking? 123_)_)(*())ŚĆ")
                    ]

# correct set of data with maximum allowed characters
testdata_correct_2_max_chars = [("qwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwert"),          
                                ("qwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwertqwertmail@domena.com"), 
                                    #this E-MAIL will fail with 'must be a well-formed email address' but is is correct. The real reason is too many chars, I would report this
                                ("+1234567890 123456789"), 
                                ("Can I have discount?Can I have discount?Can I have discount?Can I have discount?12345123451234512345"), 
                                ('''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''') #2000 chars
                             ]

# correct set of data with minimum allowed characters
testdata_correct_3_min_chars = [("a"), ("a@b"), ("12345678901"), ("abcde"), ("abcdeabcdeabcdeabcde")]

#-------------error name
# name null
testdata_bad_name_1 = [(""), ("a@b"), ("12345678901"), ("abcde"), ("abcdeabcdeabcdeabcde"), ("Name may not be blank")]

# name too long
testdata_bad_name_2 = [("9xAi3uk3GkFAy04vP4BmctzilLa4mYgmlH0o6GILa0tzBE0Vpgr1lOjyutX1ibDAQhpdqRdPjAvZCmdDzFKJktuFkfWN2Ai97plZ"), 
                            #this test will pass but I think there should be some length restrictions 
                        ("a@b"), ("12345678901"), ("abcde"), ("abcdeabcdeabcdeabcde"), 
                        ("Name must max 64 characters long")]
                                    #I made up this error message, because there is no such in the application (as described in comment above)

#-------------error email
# email null
testdata_bad_email_1 = [("a"), (""), ("12345678901"), ("abcde"), ("abcdeabcdeabcdeabcde"), ("Email may not be blank")]

# email too long
testdata_bad_email_2 = [("a"), ("a1234567890a1234567890a1234567890a1234567890a1234567890a1234567890a1234567890a1234567890@bbbbbbbb.com"), 
                            #this test will pass but I think there should be some length restrictions 
                        ("12345678901"), ("abcde"), ("abcdeabcdeabcdeabcde"), 
                        ("Email must max 128 characters long")]
                            #I made up this error message, because there is no such in the application (as described in comment above)

# email without @
testdata_bad_email_3 = [("a"), ("abcde"), ("12345678901"), ("abcde"), ("abcdeabcdeabcdeabcde"), 
                        ("Must be a well-formed email address")]
                         #this test will fail due to small letter on the beginnign in the original error message

#-------------error phone
# phone null
testdata_bad_phone_1 = [("a"), ("a@b"), (""), ("abcde"), ("abcdeabcdeabcdeabcde"), ("Phone may not be blank")]

# phone too long
testdata_bad_phone_2 = [("a"), ("a@b"), ("123456789012345678901"), ("abcde"), ("abcdeabcdeabcdeabcde"), ("Phone must be between 11 and 21 characters.")]

# phone too short                                                       
testdata_bad_phone_3 = [("a"), ("a@b"), ("1234567890"), ("abcde"), ("abcdeabcdeabcdeabcde"), ("Phone must be between 11 and 21 characters.")]

#-------------error subject
# subject null
testdata_bad_subject_1 = [("a"), ("a@b"), ("12345678901"), (""), ("abcdeabcdeabcdeabcde"), ("Subject may not be blank")]

# subject too short
testdata_bad_subject_2 = [("a"), ("a@b"), ("12345678901"), ("abcd"), ("abcdeabcdeabcdeabcde"), ("Subject must be between 5 and 100 characters.")]

# subject too long
testdata_bad_subject_3 = [("a"), ("a@b"), ("12345678901"), 
                          ("9xAi3uk3GkFAy04vP4BmctzilLa4mYgmlH0o6GILa0tzBE0Vpgr1lOjyutX1ibDAQhpdqRdPjAvZCmdDzFKJktuFkfsWN2Ai97plZ"), #101 chars
                          ("abcdeabcdeabcdeabcde"), ("Subject must be between 5 and 100 characters.")]

#-------------error message
# message null
testdata_bad_message_1 = [("a"), ("a@b"), ("12345678901"), ("abcde"), (""), ("Message may not be blank")]

# message too short
testdata_bad_message_2 = [("a"), ("a@b"), ("12345678901"), ("abcde"), ("1234567890123456789"), ("Message must be between 20 and 2000 characters.")]

# message too long
testdata_bad_message_3 = [("a"), ("a@b"), ("12345678901"), ("abcde"), 
                          ('''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'''), #2001 chars
("Message must be between 20 and 2000 characters.")]

#-------------multiple error messages at once
# message null
testdata_bad_multiple_1 = [(""), (""), ("12345"), ("abc"), ("abcdefg"), 
                          ("Message must be between 20 and 2000 characters."),
                          ("Email may not be blank"),
                          ("Subject must be between 5 and 100 characters."),
                          ("Phone must be between 11 and 21 characters."),
                          ("Name may not be blank"),
                          ("Name John"), ("john@mail.com"), ("+12345 4564564"), ("some questions that i have"), 
                          ("PYIEWNqZSjI8EDknIIcJv7Yb0jve07D7IxD5VMwDUIhkodaFSBHaF29TI5QLaphoHkOiBKuoM7eGUjH7pOaNfcZ9EpxhpJWHVl8t"),]


#-------------sql injection test data
testdata_injection_1 = [('" or ""="'), ('" or ""="'), ('" or ""="'), ('" or ""="'), ('" or ""="'), 
                           ("Phone must be between 11 and 21 characters."),
                           ("must be a well-formed email address"),
                           ("Message must be between 20 and 2000 characters.")]

testdata_injection_2 = [('" or ""="'), ('qwert@mail.com'), ('123123123123123'), ('qwertqwertqwert'), ('123123123123123123123123123123'), 
                           (""),
                           (""),
                           ("")]


