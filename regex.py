import re
import readline

try:
    readline.read_history_file('regex-history')
except IOError:
    pass

text = "During dinner, Mr. Bennet whose IP was 10.12.4.2 scarcely spoke at all; but when the guests left, he thought it time to send an email to admin@port.ac.uk and library@port.ac.uk but one at a time. And therefore started a subject in which he expected him to visit http://www.port.ac.uk/mylab, by observing that he seemed very fortunate in his patroness. Lady Catherine de Bourgh's attention to his wishes, and consideration for his phone number 07837172812, appeared very remarkable. Mr. Bennet could not have chosen a landline such as 02392 848484.  if he were in america, he should have been called on +442392848484 Mr. Collins was eloquent in her praise. The subject elevated him to more than usual solemnity of manner, and with a most important aspect he protested that he had never in his life witnessed such behaviour in a person of rank.such affability and condescension, as he had himself experienced from Lady Catherine. She had been graciously pleased to approve of both of the discourses which he had already had the honour of preaching before her. She had also asked him twice to dine at Rosings, and had sent for him only the Saturday before, to make up her pool of quadrille in the evening. Lady Catherine was reckoned proud by many people he knew, but he had never seen anything but affability in her. She had always spoken to him as she would to any other gentleman; she made not the smallest objection to his joining in the society of the neighbourhood nor to his leaving the parish occasionally for a week or two, to visit his relations. She had even condescended to advise him to marry as soon as he could, provided he chose with discretion; and had once paid him a visit in his humble parsonage, where she had perfectly approved all the alterations he had been making, and had even vouchsafed to suggest some herself.some shelves in the closet up stairs."

while True:
    print
    print "-------------------------------------"
    regex_txt = raw_input("Enter your RegEx: ")
    try:
      regex = re.compile(regex_txt)
      print
      print "RESULTS------------------"
      print regex.findall(text)
    except Exception:
      print "Invalid RegEx"

readline.add_history(regex_txt)
readline.write_history_file('regex-history')

