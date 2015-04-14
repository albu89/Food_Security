'''
@author: albu
'''
 #!/usr/bin/env python2

price = {}
price['low'] = ['price', 'coupon', 'discount', 'benefit', 'sold', 'markets', 'purchase', 'rates', 'cost', 'deal', 'funding', 'bill', 'rating', 'expensive', 'cheap']

poverty = {}
poverty['high'] = ['children', 'future', 'issue','safe', 'support', 'benefit', 'health', 'dangerous', 'poverty', 'obesity', 'changes', 'program', 'freedom', 
'syria', 'sustainability', 'donate', 'foundation', 'supplies', 'kills', 'cash']


needs = {}
needs['low'] = ['help', 'amazing', 'thanks', 'delicious', 'awesome', 'tasty', 'needed', 'nice', 'healthier', 'benefits', 'helps', 'love', 'tax', 'often', 'incredible', 'yum', 'heavenly', 'trash', 'necessary', 'enjoy', 
'smiling', 'struggle', 'disaster', 'stress', 'brilliant', 'beyond', 'yummy']

# include cooking related words in high supply
supply = {}
supply['high'] = ['available', 'coupons', 'receive', 'farming', 'production', 'imports', 'resources', 'distribution', 'processing', 'consumption', 'exports', 'mold', 'harvest', 'increase', 'rise']



predictors_dict = {'predict': predict, 'price': price, 'sentiment': sentiment, 'poverty': poverty, 'needs': needs, 'supply': supply}

if __name__ == '__main__':
    print predictors_dict
