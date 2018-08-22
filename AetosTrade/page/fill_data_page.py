#!/usr/bin/env python
#-*- coding:utf-8 -*-
from utils.get_by_local import GetByLocal
import time
class FillDataPage:
    '''获取完善资料的页面元素信息'''

    def __init__(self,driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_account_type_element(self):
        '''
        获取账户类型元素信息
        '''
        return self.get_by_local.get_element('account_type','fill_data_element')

    def get_page1_next_step_element(self):
        '''
        获取page1的下一步元素信息
        '''
        return self.get_by_local.get_element('next_step','fill_data_element')

    def get_call_element(self):
        '''
        获取称呼元素信息
        '''
        return self.get_by_local.get_element('call','fill_data_element')

    def get_name_element(self):
        '''
        获取名元素
        '''
        return self.get_by_local.get_element('name','fill_data_element')

    def get_surename_element(self):
        '''
        获取姓元素
        '''
        return self.get_by_local.get_element('surename','fill_data_element')

    def get_chinese_name_element(self):
        '''
        获取中文姓名元素
        '''
        return self.get_by_local.get_element('chinese_name','fill_data_element')

    def get_card_type_element(self):
        '''
        获取证件类型元素
        '''
        return self.get_by_local.get_element('card_type','fill_data_element')

    def get_card_no_element(self):
        '''
        获取证件号码元素
        '''
        return self.get_by_local.get_element('card_no','fill_data_element')

    def get_birth_date_element(self):
        '''
        获取出生日期元素
        '''
        return self.get_by_local.get_element('birth_date','fill_data_element')

    def get_city_element(self):
        '''
        获取城市元素
        '''
        return self.get_by_local.get_element('city','fill_data_element')

    def get_live_address_element(self):
        '''
        获取居住地址元素
        '''
        return self.get_by_local.get_element('live_address','fill_data_element')

    def get_live_date_element(self):
        '''
        获取居住年限元素
        '''
        return self.get_by_local.get_element('live_date','fill_data_element')

    def get_home_phone_element(self):
        '''
        获取住宅电话元素
        '''
        return self.get_by_local.get_element('home_phone','fill_data_element')

    def get_page2_next_step_element(self):
        '''
        获取page2的下一步元素信息
        '''
        return self.get_by_local.get_element('page2_next_step','fill_data_element')

    def get_for_exp_element(self):
        '''
        获取外汇经验选择框元素
        '''
        return self.get_by_local.get_element('home_phone','fill_data_element')

    def get_invest_freq_element(self):
        '''
        获取外汇投资经验选择框元素
        '''
        return self.get_by_local.get_element('investFreq','fill_data_element')

    def get_otherExp_element(self):
        '''
        获取其他投资经验选择框元素
        '''
        return self.get_by_local.get_element('otherExp','fill_data_element')

    def get_risk_accept_element(self):
        '''
        获取风险接受元素
        '''
        return self.get_by_local.get_element('risk_accept','fill_data_element')

    def get_isPolitic_element(self):
        '''
        获取是否直系亲属元素
        '''
        return self.get_by_local.get_element('isPolitic','fill_data_element')

    def get_isTax_element(self):
        '''
        获取是否纳税居民元素
        '''
        return self.get_by_local.get_element('isTax','fill_data_element')

    def get_isUsa_element(self):
        '''
        获取是否美国人士元素
        '''
        return self.get_by_local.get_element('isUsa','fill_data_element')

    def get_isForUsa_element(self):
        '''
        获取是否非美国人士元素
        '''
        return self.get_by_local.get_element('isForUsa','fill_data_element')

    def get_isEarnUsa_element(self):
        '''
        获取是否来自美国收入的非美国人士元素
        '''
        return self.get_by_local.get_element('isEarnUsa','fill_data_element')

    def get_page3_next_step_element(self):
        '''
        获取page3下一步元素
        '''
        return self.get_by_local.get_element('page3_next_step','fill_data_element')

    def get_business_element(self):
        '''
        获取行业元素
        '''
        return self.get_by_local.get_element('business','fill_data_element')

    def get_position_element(self):
        '''
        获取职位元素
        '''
        return self.get_by_local.get_element('position','fill_data_element')

    def get_employerName_element(self):
        '''
        获取职位元素
        '''
        return self.get_by_local.get_element('employerName','fill_data_element')

    def get_accept_data_element(self):
        '''
        获取本人确认资料真实CheckBox元素
        '''
        return self.get_by_local.get_element('accept_data','fill_data_element')

    def get_accept_person_data_element(self):
        '''
        获取个人信息披露CheckBox元素
        '''
        return self.get_by_local.get_element('accept_person_data','fill_data_element')

    def get_accept_term_element(self):
        '''
        获取接受条款CheckBox元素
        '''
        return self.get_by_local.get_element('accept_term','fill_data_element')

    def get_accept_open_form_element(self):
        '''
        获取接受客户申请表CheckBox元素
        '''
        return self.get_by_local.get_element('accept_open_form','fill_data_element')

    def get_accept_Disclaimer_element(self):
        '''
        获取接受免责声明CheckBox元素
        '''
        return self.get_by_local.get_element('accept_Disclaimer','fill_data_element')

    def get_accept_Disclosure_Statement_element(self):
        '''
        获取接受披露声明CheckBox元素
        '''
        return self.get_by_local.get_element('accept_Disclosure_Statement','fill_data_element')

    def get_accept_Policy_element(self):
        '''
        获取接受使用条款CheckBox元素
        '''
        return self.get_by_local.get_element('accept_Policy','fill_data_element')

    def get_accept_Financial_Services_Guide_element(self):
        '''
        获取接受金融服务指南CheckBox元素
        '''
        return self.get_by_local.get_element('accept_Financial_Services_Guide','fill_data_element')

    def get_accept_Risk_Warning_element(self):
        '''
        获取接受风险提示CheckBox元素
        '''
        return self.get_by_local.get_element('accept_Risk_Warning','fill_data_element')

    def get_understand_trade_element(self):
        '''
        获取理解CheckBox元素
        '''
        return self.get_by_local.get_element('understand_trade','fill_data_element')

    def get_understand_market_element(self):
        '''
        获取理解CheckBox元素
        '''
        return self.get_by_local.get_element('understand_market','fill_data_element')

    def get_understand_lever_element(self):
        '''
        获取理解CheckBox元素
        '''
        return self.get_by_local.get_element('understand_lever','fill_data_element')

    def get_understand_risk_element(self):
        '''
        获取理解CheckBox元素
        '''
        return self.get_by_local.get_element('understand_risk','fill_data_element')

    def get_fill_complete_element(self):
        '''
        获取完成元素
        '''
        return self.get_by_local.get_element('complete','fill_data_element')

    def get_upload_data_element(self):
        '''
        获取上传资料元素
        '''
        return self.get_by_local.get_element('upload_data','fill_data_element')