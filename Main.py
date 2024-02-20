from Modules.Preprocessing import Eml_to_Json
from Modules.processing.AIProcessing import AIAnalysis

phishing_emails = [
    "Dear Customer,\n\nWe regret to inform you that there has been suspicious activity detected on your account. Please click on the following link to verify your account details and prevent any unauthorized access: http://suspicious-link.com",
    "URGENT: Your account has been compromised. Please login to your account immediately and update your security information to prevent further unauthorized access.",
    "Congratulations! You've won a free vacation. Click here to claim your prize now.",
    "Your PayPal account has been temporarily suspended due to suspicious activity. Please login to verify your account information and restore access.",
    "Your bank account has been locked due to unusual activity. Click here to verify your identity and unlock your account.",
    "We have detected unauthorized access to your email account. Please verify your identity by clicking on the link below to avoid account suspension: http://phishing-link.com"
]

non_phishing_emails = [
    "Hi [Recipient],\n\nI hope this email finds you well. Attached is the report you requested yesterday. Please review it and let me know if you need any further assistance.\n\nBest regards, [Sender]",
    "Dear [Name],\n\nThank you for your recent inquiry. We appreciate your interest in our products. Please find attached the requested product catalog.\n\nBest regards, [Company]",
    "Hello [Recipient],\n\nI'm writing to follow up on our conversation last week regarding the upcoming project. Please let me know if you have any questions or need additional information.\n\nBest regards, [Sender]",
    "Dear valued customer,\n\nWe are pleased to inform you that your order has been successfully processed and will be shipped out today. You can expect to receive it within the next 3-5 business days.\n\nBest regards, [Company]",
    "Hi [Name],\n\nI wanted to reach out and thank you for your continued support. We truly appreciate your business and look forward to serving you in the future.\n\nBest regards, [Sender]"
]


phishing_emails2 = [
    "Dear Customer, Your account has been temporarily suspended due to suspicious activity. Please click on the following link to verify your identity and restore access: http://suspicious-link.com",
    "URGENT: Your password has been compromised. Please reset your password immediately by clicking on the following link: http://reset-password.com",
    "Congratulations! You've won a free gift card. Click here to claim your prize now.",
    "Your PayPal account has been locked. To unlock your account, please provide your personal information by clicking on the following link: http://unlock-account.com",
    "We have detected unauthorized access to your email account. Click here to secure your account: http://secure-account.com"
]

non_phishing_emails2 = [
    "Hi [Name], I hope this email finds you well. Attached is the agenda for our upcoming meeting. Please review it and let me know if you have any questions.",
    "Dear Customer, Thank you for your recent purchase. Your order has been successfully processed and will be shipped out shortly.",
    "Hello [Recipient], I'm writing to follow up on our previous conversation. Please find attached the documents you requested. Let me know if you need any further assistance.",
    "Hi [Name], I wanted to let you know that the event has been rescheduled. Please check your calendar for the updated date and time.",
    "Dear valued customer, We appreciate your feedback. Please take a moment to complete our survey and share your thoughts with us."
]



for email in phishing_emails:
    prediction = AIAnalysis.ai_bodytext_analysis(input_text=email)
    print(f"Phishing Email Prediction: {prediction}\n")

for email in non_phishing_emails:
    prediction = AIAnalysis.ai_bodytext_analysis(input_text=email)
    print(f"Non-Phishing Email Prediction: {prediction}\n")

for email in phishing_emails2:
    prediction = AIAnalysis.ai_bodytext_analysis(input_text=email)
    print(f"Phishing Email Prediction: {prediction}\n")

for email in non_phishing_emails2:
    prediction = AIAnalysis.ai_bodytext_analysis(input_text=email)
    print(f"Non-Phishing Email Prediction: {prediction}\n")


#percentages of correct predictions for each class:
# Phishing: 7/9 ≈ 77.78%
# Legitimate: 4/6 ≈ 66.67%

#data source might be the issue need to work on that