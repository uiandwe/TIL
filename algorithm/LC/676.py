# -*- coding: utf-8 -*-
from typing import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            if self.searchTrie(self.root, searchWord[:i]+"*"+searchWord[i+1:], searchWord[i]):
                return True
        return False

    def searchTrie(self, node, word, char):
        if len(word) == 0:
            if node.end:
                return True
            return False

        for d in node.children.keys():
            if (word[0] != '*' and word[0] == d) or (word[0] == '*' and char != d):
                if self.searchTrie(node.children[d], word[1:], char):
                    return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
dictionary = ["hello", "leetcode"]
obj = MagicDictionary()
obj.buildDict(dictionary)
search_word = ["", "hello", "hhllo", "hell", "leetcoded"]
#              False  False  True     False   False
for word in search_word:
    print(obj.search(word))
print("=======================================")
dictionary = ["a","b","ab","abc"]
obj = MagicDictionary()
obj.buildDict(dictionary)
search_word = ["a","b","ab","abc", "cba", "abb"]
#             True True False False False True
for word in search_word:
    print(obj.search(word))
print("=======================================")
dictionary = ["wyrlwlivuxfnkvzvduypntvlnsvgjrbkoymotuonwokqvqnqpkatpqkptpkzmoq","onirxfxqbljpcyxmkhsfbtcsdipuhksyujsklothmbkgaudnmjcrpgzrtfomylzqthkuovatylefzeappn","cchslkxgpysqjglecvuongodqbxt","oupaaniblfehmuhyuwerqvlvdrhmjaihvbuuaxmmritpi","ptdrylqmpdcwwhkkacyysmcknmyxljgitrqkvbnscpmqhudmwqlfwlznwmmjuvscowredkhhhrtseuuhm","skmyqhdtciiodzyk","tzbzgwcrskuzo","ux","ntyjmltpqyzlurqzgoasfzkvqdwrfvaa","in","zdbcyjrklxsjdlspfnkjhdezkskldtjogjpeguxktkygkfcipwobgujpsgoonjnsymvjzsyxbbowryit","vjzraatoidkpeysubnzyghex","fsmygqhxnhzwibnfwbpzmwqaboauybcgfecehttdfcjpoqvntzbevdugvfkhreghyphwptldxeostrduhuh","jnslcrkmgsfgyeueargdexsmyreqkrmxbdqmxyllzr","vpjdbmvrubabvwkltqaazzwnfwhwyfuskvfqmjsqqcudbrijcbwazlvkbenrskn","xpuneikzvuadjdnretryacjmwnelidaprrbb","djtxglaypnumdlrkgxdpcblxpiwpmksglyffbqigfqyeimmsnqwwyhmwpxujmejhgekbukihngbqlrcemuxj","gluzitmxytthhfhchtxlrtonqfrvlhmagijhnokoghfttws","uircoqjmuotdewoepntvppyxnsapstrrzjgojlinzcltpiwsgneujpurzxisibgzufyjv","dnrhugzftyrizlfrlrrtiqpnjhwyzvmkijpdwdnqnjzgmrwuvqshurhdjlgpysiw","czoltjgidnavnfzfwtwgoveyqbehjzfprvugpeeyhcdkooenxsuulkhqekanyaghy","hegdgsqfckptnpjylyusypovacetppcqfmiyyrswdwuvzhetucvfshdtqcxmuiqxyydphghhdvzhonkegxflxxoegfrahnkqzdr","abfelpzwjna","feipzwojrhfyfemhfkwqfrnhpsigfnminqmgowpuwaccvxnmzfbklo","jhpcoqm","qyaquqzdgggxnrxgbmphy","dqqtmkujcpjiqixaedctqkfnbctwhmotrjbyxoplkkdllj","iupdcciklryyufbpmrgiywltpkmeqfgitfcdjgpbkupxyet","llgvgfwdblgbqmiuoahqpaqjdopxichcjuuxmltnzxqgiezkwhnfrlfnviwppvbqsgavkfudfyobl","gufjwsskpbgvaqtkfghwcavzchyhqhyaordzusmkmzhigzcyrgw","xlijejvicoccycgudcaszsrgoufjogvagyqvnnsfwrbzkqlhhraussrbzsi","qyltkwknzzjgedjj","mqargegjoagrchkzcutnudhwswdvlagwrm","gofpdibkkaaklxhjjvgxenttfktljiadjqdkcysteyorvtvsweytzaraivrvhatydmvnzjbemajed","ylfqomkvofdfzjlxgwwaiijjlcsrg","peypbguojlmumynymjsl","zxbehgiwzqtsqiwzgwnshxznmbzmewwwvdfzdvjhiwtlmqwcopjoeqnyjiwrenxzkac","ieddfzkavdvaodzteevlvkwhqyqtodwrnpdyzsgygrwrevdqyopnmyimcinpgwivflntexbozheqix","abxsckranbvxck","rxuauxdapvcbf","nkcowhrktuzmvjhvhyrdl","gjdxucsekbgpfuwmigecyyinufeqvmimjwfidscdokrlhcryfrkajzrzsofgzzfhwjvmruxlearqqedrrcmd","wxropbkmmpltxupsdfpbwbdsligunyhghalcymxoafpxgpmvfeolwucymndxfkulifqehpkzwwfjxdjbbwiqhxthziyqhd","rbyjugvhimvqlpwcheexlfjyhjqvhlbwaraxuzkksxuxlxlnxkdtxrzdajphllldtlnodsoyxekvjauifgwintuegfzhtiky","kmxhijbnohkfezxfkjnjgcdcbtsnvjdnsxxgiouadodqliktxaxrbzo","wnujflblzfdnemhehvynvfaxvarubdcnmtheblunhoefbdiaikbidxxddpzjlvaltwnmzjexuyypmmuviuabjeuphnz","aidvhkxbvnonaiobrbqjkfgqrganbucdtqqdfke","ajumuxbldhjwjemgfetktaolsvmfmrxdhykdthatzuevsuhbifjeei","xzmespyzhwebfbkcrixosiynjrgtevioxvlzfmmvesouqrmlwzaidtxeongulywcegecuzz","vxmxnntwcnpykaykmfozctllaeaicbotpwcklshmdaioivfqlwezww","vfltyutmdxfdstwsskufkdf","rjkkvzuoeapdaafysvceslmjkyecuehpmgwdzgbmvqyzrdxjcafptbhzeudkkxivlwcsuewblpmvuplqkthuhqhzzdfqhhaixq","zpfygiqxwmvamzbwruuyolncwsrixgfzsuxmgtmvnksmnsijzudoisvxxwfkiidtzuwlfucuicocpsqecdnfyebt", "ae"]
# dictionary = ["wa", "af", "oe", "ii", "zz", "ll"]
obj = MagicDictionary()
obj.buildDict(dictionary)
search_word = ["yeypbguojlmumynymjsl"] #true
for word in search_word:
    print(obj.search(word))
