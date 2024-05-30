from django import forms
from captcha.fields import CaptchaField

from core.components.CaptchaComponent import CustomCaptchaTextInput
from page.models import ContactUs


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        error_messages={
            'required': 'نام  و نام خانوادگی را وارد کنید',
            'max_lenght': 'نام و نام خانوادگی نمیتواند بیشتر از 50 کاراکتر باشد'

        },
        widget=forms.TextInput(attrs={
            'class': 'clear full',
            'placeholder': 'نام و نام خانوادگی',
            'required': 'required'
        }),
        required=True
    )
    subject = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={
        'class': 'clear full', 'placeholder': 'موضوع', 'required': 'required'
    }),
     required=True
    )
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={
            'class': 'clear full',
            'placeholder': 'ایمیل',
            'required': 'required'

        }), required=True)
    message = forms.CharField(label='متن پیام', widget=forms.Textarea(
        attrs={
            'class': 'clear full',
            'placeholder': 'متن پیام',
            'required': 'required'

            # 'rows': 5
            # 'id': 'message'
        }),
        required=True
     )
    captcha = CaptchaField(
        widget=CustomCaptchaTextInput,
        error_messages={'required': 'کد امنیتی را وارد کنید'},  # تغییر در این پیام خطا
        label='کد امنیتی',  # اضافه کردن برچسب برای فیلد Captcha
        required=True  # تنظیم فیلد Captcha به عنوان ضروری
    )

    class Meta:
        model = ContactUs
        fields = '__all__'
