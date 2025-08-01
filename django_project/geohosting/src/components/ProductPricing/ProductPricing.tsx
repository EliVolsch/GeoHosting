import React from "react";
import { useNavigate } from "react-router-dom";
import {
  Box,
  Button,
  Heading,
  Image,
  List,
  ListItem,
  Text,
  Tooltip,
  useDisclosure,
} from "@chakra-ui/react";
import { CheckIcon } from "@chakra-ui/icons";
import { Package, Product } from "../../redux/reducers/productsSlice";
import {
  formatPrice,
  packageIndicator,
  packageName,
} from "../../utils/helpers";
import LoginForm from "../LoginForm/LoginForm";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/store";

export interface PackageProps {
  product: Product;
  pkg: Package;
}

const ProductPricing: React.FC<PackageProps> = ({ product, pkg }) => {
  const navigate = useNavigate();
  const available = product.available;
  const { isOpen, onOpen, onClose } = useDisclosure();
  const { token } = useSelector((state: RootState) => state.auth);

  const handleCheckout = () => {
    localStorage.setItem(
      "selectedProduct",
      JSON.stringify({
        product,
        pkg,
      }),
    );
    if (token) {
      navigate("/checkout/configuration", { state: { product, pkg } });
    } else {
      onOpen();
    }
  };

  const isBestValue = pkg.name.toLowerCase().includes("medium");
  const packageLevel = packageName(pkg);
  return (
    <Box
      key={pkg.id}
      height={"auto"}
      backgroundColor={"white"}
      borderRadius={15}
      padding="30px"
      display={"flex"}
      justifyContent={"flex-start"}
      alignItems={"center"}
      flexDirection="column"
      width={"360px"}
      boxShadow="0px 4px 6px rgba(0, 0, 0, 0.2)"
      position="relative"
      borderColor="blue.500"
      borderWidth={isBestValue ? 1 : 0}
    >
      {/* Coming Soon Banner */}
      {!available && (
        <Box position="absolute" top="-35px" right="-35px" zIndex={999}>
          <Image
            src="/static/images/Coming_Soon_Banner.png"
            alt="Coming Soon"
            width={185}
          />
        </Box>
      )}
      <Box>
        <Heading
          as="h4"
          fontSize={24}
          padding="15px"
          textAlign="center"
          fontStyle={"bold"}
        >
          {product.name} {packageLevel}
        </Heading>
      </Box>
      <Box
        padding="5px"
        fontSize={14}
        textAlign="center"
        fontStyle={"bold"}
        width="135px"
        borderRadius="45px"
        backgroundColor={isBestValue ? "blue.500" : "#57A0C750"}
        color={isBestValue ? "white" : "unset"}
      >
        {packageIndicator(pkg)}
      </Box>
      {/* Blurred content if not available */}
      <Box
        my={5}
        filter={!available ? "blur(4px)" : "none"}
        position="relative"
        width="100%"
        textAlign="center"
      >
        <Box
          flexDirection={"row"}
          display={"flex"}
          alignItems={"end"}
          justifyContent="center"
        >
          <Text
            fontSize={{ base: "35", sm: "45", md: "32", xl: "45" }}
            fontWeight={"bold"}
            color={"gray.600"}
            lineHeight={10}
          >
            {!available ? pkg.currency : formatPrice(pkg.price, pkg.currency)}
          </Text>
        </Box>
        <Box
          fontSize={{ base: "15", sm: "25", md: "12", xl: "25" }}
          color={"gray.600"}
        >
          / month
        </Box>
      </Box>
      <Box
        mt={5}
        textAlign="center"
        width={{ base: "60%", md: "80%", xl: "60%" }}
        alignItems="center"
        filter={!available ? "blur(4px)" : "none"}
      >
        <Text fontWeight={"bold"} fontSize={18}>
          {packageLevel} Features
        </Text>
        <List spacing={2} mt={3} pl={5}>
          {pkg.feature_list &&
            pkg.feature_list["spec"] &&
            Object.entries(pkg.feature_list["spec"]).map(
              ([key, value]: any) => {
                if (!value) {
                  return;
                }
                return (
                  <ListItem key={key} display="flex" alignItems="center">
                    <CheckIcon color="blue.500" mr={2} /> {value}
                  </ListItem>
                );
              },
            )}
        </List>
      </Box>
      <Box mt={10} width="100%" pl={7} pr={7}>
        <Tooltip label="Product is not available" isDisabled={available}>
          <Button
            size={"xl"}
            width="100%"
            backgroundColor={
              packageLevel === "Gold" ? "customOrange.500" : "blue.500"
            }
            color={"white"}
            fontWeight={"bold"}
            paddingTop={5}
            paddingBottom={5}
            onClick={handleCheckout}
            isDisabled={!available}
            _disabled={{
              backgroundColor:
                packageLevel === "Gold" ? "customOrange.500" : "blue.500",
              cursor: "not-allowed",
              opacity: 0.6,
            }}
            _hover={{
              filter: "brightness(1.1)",
              cursor: available ? "pointer" : "not-allowed",
            }}
            transition="filter 0.3s ease"
          >
            {`Order ${packageLevel}`}
          </Button>
        </Tooltip>
      </Box>
      <LoginForm
        isOpen={isOpen}
        onClose={onClose}
        onSuccess={() => {
          navigate("/checkout/configuration", { state: { product, pkg } });
        }}
      />
    </Box>
  );
};

export default ProductPricing;
