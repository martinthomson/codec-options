#!/usr/bin/python

CODECS = [
    'H.264',
    'VP8',
    'H.263',
    'H.261',
    'Theora',
]

CHOICES = ['-', 'SHOULD', 'MUST']
LINE = 0

must_subsets = []
should_subsets = []

def print_ctx(ctx):
    res = {
        '-':[],
        'MUST':[],
        'SHOULD':[]
    }
    
    for c in ctx:
        res[c[1]].append(c[0])

    if len(res['SHOULD'])==0 and len(res['MUST']) == 0:
        return

    str = ""
    if len(res['MUST']):
        str += "MUST: " + " ".join(res['MUST'])

    if len(res['SHOULD']):
        if str != "":
            str += "; "
        
        str += "SHOULD: " + " ".join(res['SHOULD'])

    print str

    if (len(res['SHOULD']) == 0):
        for i in range(1,len(res['MUST'])):
            must_subsets.append("MUST do %d of {%s}"%(i, ", ".join(res['MUST'])))

    if (len(res['MUST']) == 0):
        for i in range(1,len(res['SHOULD'])):
            should_subsets.append("SHOULD do %d of {%s}"%(i, ", ".join(res['SHOULD'])))

        
def do_codec(ctx, lst):
    global LINE
    for c in CHOICES:
        ctx_tmp = ctx[:]
        ctx_tmp.append([lst[0], c])
        
        if (len(lst) == 1):
            print_ctx(ctx_tmp)
        else:
            do_codec(ctx_tmp, lst[1:])


do_codec([], CODECS)


print "\n".join(should_subsets)
print "\n".join(must_subsets)

