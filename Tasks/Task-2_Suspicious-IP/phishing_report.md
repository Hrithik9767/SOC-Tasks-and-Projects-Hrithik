# Phishing Email Analysis Report

## Sample Email Summary

**Subject:** Urgent: Your Apple ID has been locked  
**Sender Email:** support@apple.fake.com  
**Date:** June 22, 2025  
**Link Provided:** https://apple.verify-user.com/login  

---

## Phishing Indicators Found

### 1. **Email Spoofing**
- Sender's address (`support@apple.fake.com`) is **not a legitimate Apple domain**.
- A genuine Apple email would use `@apple.com`.

### 2. **Suspicious Link**
- The link text seems to be from Apple, but hovering reveals `https://apple.verify-user.com/login`, which is **not an Apple domain**.
- Could lead to a credential harvesting page.

### 3. **Urgent Language**
- "Failure to verify within 24 hours will result in permanent account suspension" creates panic and forces users to act without thinking.

### 4. **Generic Greeting**
- “Dear Customer” instead of personalized greeting. Legit companies usually address users by name.

### 5. **Grammar & Style**
- The email has inconsistent tone (too formal and threatening). Legit Apple mails are usually concise and polite.

---

## Header Analysis

(We are using this tool here [MxToolbox](https://mxtoolbox.com/EmailHeaders.aspx))

- **SPF check:** Failed
- **DKIM:** Not signed
- **DMARC:** No policy
- **Received from:** Unknown mail relay
- **IP reputation:** Blacklisted IP detected

---

## Conclusion

This email is clearly a phishing attempt. It uses **spoofed sender**, **malicious links**, and **threatening language** to manipulate the recipient.  

### Recommendation:
- Never click on suspicious links.
- Always verify sender addresses.
- Report the email to IT/security or your email provider.

