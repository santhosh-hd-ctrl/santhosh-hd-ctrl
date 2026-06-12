#!/usr/bin/env python3
"""
Dynamic Profile README Generator
Creates an awesome GitHub profile README with dynamic content
"""

import os
import json
from datetime import datetime


def generate_profile_readme():
    """Generate dynamic profile README"""
    
    readme_content = """# Hi 👋, I'm Santhosh H D
A dedicated developer from India 🇮🇳

## 🌱 Currently Learning
- Advanced Python concepts
- Full-stack development
- Data Structures & Algorithms
- Database optimization

## 👨‍💻 What I Do
I'm a versatile developer working on various projects involving **Backend Development**, **Web Development**, and **Database Management**. I enjoy solving real-world problems through code and continuously improving my skills.

## 📂 Projects & Experience

### 🚀 Key Projects:
- **[Internship](https://github.com/santhosh-hd-ctrl/Internship)** - Comprehensive collection of Java projects, SQL databases, and web development work including ChatSphere, Hospital Management, and more
- **[Deloitte](https://github.com/santhosh-hd-ctrl/Deloitte)** - Python-based projects and automation
- **[Python Learning](https://github.com/santhosh-hd-ctrl/python)** - Learning Python from basics and implementing core concepts

## 💻 Languages and Tools:

**Programming Languages:**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- ![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)

**Database & Backend:**
- ![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
- ![Database Design](https://img.shields.io/badge/Database%20Design-4479A1?style=for-the-badge&logo=database&logoColor=white)

**Tools & Platforms:**
- ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
- ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

## 🎯 Key Skills:
✅ Object-Oriented Programming (Java)  
✅ Database Design & SQL Queries  
✅ Backend Development  
✅ Problem Solving & Algorithms  
✅ Data Processing & Analysis  
✅ Web Development  
✅ Custom Annotations & Validation  

## 📊 GitHub Stats:
![Santhosh's GitHub stats](https://github-readme-stats.vercel.app/api?username=santhosh-hd-ctrl&show_icons=true&theme=radical)

## 📈 Most Used Languages:
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=santhosh-hd-ctrl&layout=compact&theme=radical)

## 🏆 Notable Work:
- **Java Projects:** Calculator apps, Employee management, Student grading systems, Login validation
- **Database Projects:** Food delivery systems, Hospital management, Product databases
- **Web Development:** ChatSphere chat application, Nexus Glass & Website projects
- **Python:** Automation scripts and learning projects

## 📚 Learning Path:
I continuously work on coding challenges and build projects to strengthen my understanding of:
- Data Structures & Algorithms
- Object-Oriented Design Patterns
- Advanced Database Management
- Full-Stack Development
- System Design

## 💬 Ask me about:
- **Apps & Software Development**
- **Backend Architecture**
- **Database Design & Optimization**
- **Java Programming**
- **Python Scripting**
- **Web Development**

## 📫 Get in Touch:
Feel free to reach out if you want to collaborate, discuss tech, or work on interesting projects!

**Email:** santhoshhd.in@gmail.com  
**GitHub:** [@santhosh-hd-ctrl](https://github.com/santhosh-hd-ctrl)

---

⭐️ If you find my work interesting, consider giving my repositories a star!  
🔗 Connect with me and let's build something amazing together!

*Profile README auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ Profile README generated successfully!")


if __name__ == '__main__':
    generate_profile_readme()
