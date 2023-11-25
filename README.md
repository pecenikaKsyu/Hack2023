# Hackathon 2023 
## Human Trafficking 
### Team: Alien Algorithms
#### Students: 
**Ceban Dan**
**Cius Iurie**
**Foros Valentin** 
**Matvei Stephania**
**Wu Ksenia** 

Human Trafficking is one of the major concerns in the society. Our team suggests a strategy that takes advantage of artificial intelligence's powerful computing capacity to address the problem in light of its recent explosion.

#### About 
A deep learning-based system that is able to identify any suspicious activity by analyzing the camera's live video in real time. The closest police stations and hospitals can receive information, such as the incident's location.

**What is considered anomalous activity?**
Any activity which differs from a normal activity above a calculated threshold can be marked as anomalous activity. For example - A busy road in city can be considered as a normal activity whereas riots or voilent activites on the same roads will be considered anomalous.

### Solution
The solution our team sugests to use Generative Adversarial Nets (GANs) which are trained using normal frames and corresponding optical-flow images in order to learn an internal representation of the scene normality. As it was mentioned, our GANs are trained with only normal data, thus, they are not able to generate abnormal events. At testing time the real data is compared with both the appearance and the motion representations reconstructed by our GANs and abnormal areas are detected by computing local differences.

### How to run 