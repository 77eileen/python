-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: faq
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hyb_tbl`
--

DROP TABLE IF EXISTS `hyb_tbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hyb_tbl` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(100) DEFAULT 'Hybrid',
  `H_Q` mediumtext NOT NULL,
  `H_A` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hyb_tbl`
--

LOCK TABLES `hyb_tbl` WRITE;
/*!40000 ALTER TABLE `hyb_tbl` DISABLE KEYS */;
INSERT INTO `hyb_tbl` VALUES (1,'Hybrid','하이브리드 차량 12V 배터리 방전 시 어떻게 해야 하나요?','하이브리드 차량 (K5 하이브리드 / K8 하이브리드 / 스포티지 하이브리드) 12V 배터리 방전 시 충전 방법은 아래와 같습니다. 핸들 좌측 하단에 보면 [12V BATT RESET] 버튼이 있습니다. 해당 버튼을 누르고 15초 이내에 시동을 거신 후, 주행 가능 표시등 \'READY\'가 켜진 상태에서 30분 동안 정차하거나 주행을 하게 되면 배터리가 충전됩니다. * 도어가 닫혀있을 때 12V 배터리가 방전이 되면, 도어 핸들 커버를 탈거 후 비상키로 도어 잠금 해제를 하시면 됩니다. * 아래 링크 접속하시면 하이브리드 12V 배터리 리셋 버튼 활용방법에 관한 영상을 보실 수 있습니다.\n하이브리드 긴급 충전 리셋 버튼 사용법'),(2,'Hybrid','쏘렌토 하이브리드(4WD) 안전 하차 보조(SEA, 전자식 차일드 락 연동)은 어떤 기능인가요?','차량이 정차한 후에 탑승자가 차에서 내리려고 도어를 여는 순간 후측방의 차량을 인식하여\n충돌 위험이 판단되면 경고문 표시와 경고음 등으로 운전자에게 알려주는 기능입니다.\n추가적으로, 전자식 차일드 락이 작동된 상태에서 후측방의 차량을 인식하여 충돌 위험이 판단되면\n운전자가 차일드 락 버튼을 눌러도 차일드 락이 해제되지 않아 뒷좌석 탑승자가 도어를 여는 것을 방지합니다.'),(3,'Hybrid','하이브리드 차종 스마트 모드 선택 후 시동을 껐다 켜면 모드가 변하나요?','하이브리드 차종의 2WD의 경우\n· 「DRIVE MODE」 또는 「DRIVE / TERRAIN」 노브를 돌려 SMART 모드를 선택하면 계기판에 「SMART」 표시등이 켜집니다.\n· SMART 모드는 시동을 끄고 다시 걸어도 SMART 모드가 유지됩니다.\n· SMART 모드에 진입하면 변속 패턴, 엔진 토크, 구동력 배분 등이 운전 성향에 따라 자동으로 제어됩니다.\n* 단, 하이브리드 차종의 4WD의 경우 SMART 모드를 작동시킨 후, 다시 시동을 걸면 ECO 모드로 돌아가오니,\n필요할 경우 다시 SMART 모드를 선택하십시오.'),(4,'Hybrid','하이브리드 구동 원리는 무엇인가요?','하이브리드 차량은 두 가지 이상의 동력원(가솔린엔진과 모터)를 설치하고, 주행상태에 따라 가솔린 엔진 또는 모터의 동력을 이용하여 운영되는 자동차입니다.');
/*!40000 ALTER TABLE `hyb_tbl` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-24 12:27:57
